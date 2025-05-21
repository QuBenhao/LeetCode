import argparse
import logging
import os
import random
import re
import subprocess
import sys

from dotenv import load_dotenv

from daily_auto import write_question

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from python.constants import constant
import python.lc_libs as lc_libs
from python.utils import get_default_folder, format_question_id, check_cookie_expired

PROBLEM_MD = "problem.md"
PROBLEM_MD_ZH = "problem_zh.md"


def back_fill_ratings(args):
    def process_each(dir_path, problem_id: str):
        if not os.path.isdir(dir_path):
            return
        rating = lc_libs.get_rating(problem_id)
        if not rating:
            logging.debug("Rating not found for problem id: %s", problem_id)
            return
        problem_file_path = os.path.join(dir_path, PROBLEM_MD)
        if os.path.exists(problem_file_path):
            with open(problem_file_path, "r") as f:
                lines = f.read().split("\n")
            if not lines:
                logging.warning("Empty file: %s", problem_file_path)
            else:
                if " [Rating" in lines[0]:
                    lines[0] = lines[0].split(" [Rating")[0]
                lines[0] += " [Rating: {:.2f}]".format(rating)
                with open(problem_file_path, "w") as f:
                    f.write("\n".join(lines))
                logging.info("Rating back filled for problem id: %s", problem_id)
        problem_file_path_zh = os.path.join(dir_path, PROBLEM_MD_ZH)
        if os.path.exists(problem_file_path_zh):
            with open(problem_file_path_zh, "r") as f:
                lines = f.read().split("\n")
            if not lines:
                logging.warning("Empty file: %s", problem_file_path_zh)
                return
            if " [Rating" in lines[0]:
                lines[0] = lines[0].split(" [Rating")[0]
            if " [难度分" in lines[0]:
                lines[0] = lines[0].split(" [难度分")[0]
            lines[0] += " [难度分: {:.2f}]".format(rating)
            with open(problem_file_path_zh, "w") as f:
                f.write("\n".join(lines))
            logging.debug("Rating back filled for CN problem id: %s", problem_id)

    root_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    try:
        load_dotenv()
    except Exception as _:
        logging.error("Load Env exception", exc_info=True)
    problem_folder = os.getenv(constant.PROBLEM_FOLDER, get_default_folder())
    logging.info("Processing Problem folder: %s", problem_folder)
    if args.problem_id:
        question_id = format_question_id(args.problem_id)
        process_each(os.path.join(root_path, problem_folder, f"{problem_folder}_{question_id}"), question_id)
        return

    for root, dirs, files in os.walk(str(os.path.join(root_path, problem_folder))):
        if dirs:
            for d in list(dirs):
                if not d.startswith(f"{problem_folder}_"):
                    dirs.remove(d)
                    logging.debug("Skip folder: %s", d)
        for file in files:
            if file == PROBLEM_MD or file == PROBLEM_MD_ZH:
                process_each(root, os.path.basename(root).split(f"{problem_folder}_")[-1])
                break


def lucky_main(languages, problem_folder, category="algorithms"):
    def process_problem(root_path, question: dict, langs) -> bool:
        question_id = format_question_id(question["frontendQuestionId"])
        if question.get("paidOnly", False):
            logging.warning("Paid problem: %s", question_id)
            return False
        dir_path = os.path.join(root_path, problem_folder, f"{problem_folder}_{question_id}")
        if not os.path.exists(dir_path):
            logging.info("Found: %s", question_id)
            os.makedirs(dir_path, exist_ok=True)
            success_languages = write_question(root_path, dir_path, problem_folder,
                                               question_id, question["title"], question["titleSlug"], langs)
            logging.debug("Success languages: %s", success_languages)
            for lang in success_languages:
                cls = getattr(lc_libs, f"{lang.capitalize()}Writer", None)
                if not cls:
                    continue
                obj: lc_libs.LanguageWriter = cls()
                obj.change_test(root_path, problem_folder, question_id)
            return True
        return False

    total = lc_libs.get_questions_total(category)
    number = random.randint(1, total)
    logging.info("Random For Problem folder: %s [%d]", problem_folder, number)
    questions = lc_libs.get_questions_by_number(number, category)
    if not questions:
        logging.error(f"No question found for number: {number}")
        return 1
    central = min(number, 49)
    rpath = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    left = right = central
    while left >= 0 or right < len(questions):
        if right < len(questions):
            if process_problem(rpath, questions[right], languages):
                return 0
        if left == right:
            left -= 1
            continue
        if left >= 0:
            if process_problem(rpath, questions[left], languages):
                return 0
        left -= 1
        right += 1
    logging.warning("All problems are solved in random locations, flag: %d", number)
    return 1


def lucky(args):
    try:
        load_dotenv()
    except Exception as _:
        logging.error("Load Env exception", exc_info=True)
    languages = os.getenv(constant.LANGUAGES, "python3").split(",")
    problem_folder = os.getenv(constant.PROBLEM_FOLDER, get_default_folder())
    lucky_main(languages, problem_folder, args.category)


def remain_main(cookie, languages, problem_folder, status="TRIED", category="all-code-essentials"):
    if not cookie:
        logging.error("Cookie is needed for remaining questions.")
        return 1
    if check_cookie_expired(cookie):
        logging.warning("LeetCode cookie may have expired; please check!")
    remains = lc_libs.get_questions_by_status(status, category, True, cookie=cookie)
    if remains is None:
        logging.error("Failed to get remain problems.")
        return 1
    if not remains:
        logging.warning("No remain problems found.")
        return 1
    logging.info("Remain problems: %d", len(remains))
    pick = random.choice(remains)
    question_id = format_question_id(pick["frontendQuestionId"])
    logging.info("Pick problem: [%s].%s", pick["frontendQuestionId"], pick["title"])
    root_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    dir_path = os.path.join(root_path, problem_folder, f"{problem_folder}_{question_id}")
    if os.path.exists(dir_path):
        logging.warning("Folder already exists: %s", dir_path)
        return 1
    os.makedirs(dir_path, exist_ok=True)
    results = write_question(root_path, dir_path, problem_folder, question_id,
                             pick["title"], pick["titleSlug"], languages)
    logging.info("Problem created: %s", question_id)
    logging.debug("Success languages: %s", results)
    return 0


def remain(args):
    try:
        load_dotenv()
    except Exception as _:
        logging.error("Load Env exception", exc_info=True)
    problem_folder = os.getenv(constant.PROBLEM_FOLDER, get_default_folder())
    langs = os.getenv(constant.LANGUAGES, "python3").split(",")
    cookie = os.getenv(constant.COOKIE)
    remain_main(cookie, langs, problem_folder, args.status, args.category)


def clean_empty_java_main(root_path, problem_folder, daily: bool = False):
    question_id = None
    if daily:
        question_id = lc_libs.get_daily_question()["questionId"]

    total_remove = 0
    for root, dirs, files in os.walk(str(os.path.join(root_path, problem_folder))):
        if dirs:
            for d in list(dirs):
                if not d.startswith(f"{problem_folder}_"):
                    dirs.remove(d)
                    logging.debug("Skip folder: %s", d)
        for file in files:
            if not file.endswith(".java"):
                continue
            if daily and root.endswith(f"{problem_folder}/{problem_folder}_{question_id}"):
                logging.info("Keep daily java file: %s", os.path.join(root, file))
                continue
            with open(os.path.join(root, file), "r") as f:
                content = f.read()
                if content.count("return ") > 1:
                    continue
                logging.info("Remove empty java file: %s, %s", os.path.join(root, file), content)
                total_remove += 1
                os.remove(os.path.join(root, file))
    logging.info("Removed %d empty java files", total_remove)


def clean_empty_java(args):
    root_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    problem_folder = os.getenv(constant.PROBLEM_FOLDER, get_default_folder())
    clean_empty_java_main(root_path, problem_folder, args.daily)


def clean_error_rust_main(root_path, problem_folder, daily: bool = False):
    def remove_rust_file(_problem_id: str):
        nonlocal explored, total_remove, all_removed_problems, question_id, cur_error
        if _problem_id in explored:
            return
        explored.add(_problem_id)
        if daily and _problem_id == question_id:
            logging.info("Keep daily rust error file: %s", _problem_id)
            return
        cur_error += 1
        file_path = os.path.join(root_path, problem_folder, f"{problem_folder}_{_problem_id}", "solution.rs")
        cargo_path = os.path.join(root_path, problem_folder, f"{problem_folder}_{_problem_id}", "Cargo.toml")
        if os.path.exists(file_path):
            os.remove(file_path)
            os.remove(cargo_path)
            all_removed_problems.add(_problem_id)
            logging.info("Remove error rust file: %s", file_path)
            total_remove += 1
        else:
            logging.warning("Rust file not found: %s", file_path)

    question_id = None
    if daily:
        question_id = lc_libs.get_daily_question()["questionId"]

    total_remove = 0
    explored = set()
    all_removed_problems = set()
    cur_error = -1
    while cur_error != 0:
        res = subprocess.run(
            ["cargo", "test", "--package", "leetcode", "--test", "solution_test", "test", "--no-fail-fast"],
            check=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=60)
        if res.returncode == 0:
            logging.info("Cargo test passed, %s", res.stdout.decode("utf-8"))
            break
        stderr = res.stderr.decode("utf-8")
        if "error:" not in stderr:
            logging.error("Cargo test failed, but no error found. %s", stderr)
            break
        cur_error = 0
        lines = stderr.split("\n")
        need_to_find = False
        for line in lines:
            if not need_to_find and not re.match(r"error(\[[0-9A-Z]+\])?:", line):
                continue
            if need_to_find and (pid := re.search(rf"{problem_folder}_([0-9A-Z_]+)", line)):
                need_to_find = False
                remove_rust_file(pid.group(1))
                continue
            if problem_id_match := re.search(r"solution_([0-9A-Z_]+)", line):
                remove_rust_file(problem_id_match.group(1))
            else:
                need_to_find = True
            logging.debug("Cargo test error: %s", line)
        if cur_error == 0:
            break
        with open(os.path.join(root_path, "Cargo.toml"), "r") as f:
            lines = f.read().split("\n")
        new_lines = []
        for line in lines:
            problem_id_match = re.search(rf"/{problem_folder}_([0-9A-Z_]+)", line)
            if problem_id_match and problem_id_match.group(1) in all_removed_problems:
                continue
            new_lines.append(line)
        with open(os.path.join(root_path, "Cargo.toml"), "w") as f:
            f.write("\n".join(new_lines))
    if not total_remove:
        logging.info("No error rust files found.")
        return

    logging.info("Removed %d error rust files", total_remove)

def clean_error_rust(args):
    root_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    problem_folder = os.getenv(constant.PROBLEM_FOLDER, get_default_folder())
    if not os.path.exists(os.path.join(root_path, problem_folder)):
        logging.error("Problem folder not found: %s", problem_folder)
        return
    clean_error_rust_main(root_path, problem_folder, args.daily)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format=constant.LOGGING_FORMAT, datefmt=constant.DATE_FORMAT)
    parser = argparse.ArgumentParser()
    sub_parser = parser.add_subparsers()
    bfr = sub_parser.add_parser("rating", help="Back fill ratings")
    bfr.add_argument("-p", "--problem_id", required=False, default=None, help="Add specified Problem id only.")
    bfr.set_defaults(func=back_fill_ratings)
    ly = sub_parser.add_parser("lucky", help="Lucky")
    ly.add_argument("-c", "--category", required=False, default="algorithms",
                    help="Add specified problem category only.")
    ly.set_defaults(func=lucky)
    rm = sub_parser.add_parser("remain", help="Remain")
    rm.add_argument("-c", "--category", required=False, default="algorithms",
                    help="Add specified problem category only.")
    rm.add_argument("-s", "--status", required=False, choices=["TRIED", "AC", "NOT_STARTED"],
                    default="TRIED", help="Add specified problem status only.")
    rm.set_defaults(func=remain)
    clean_java = sub_parser.add_parser("clean_java", help="Clean empty java files")
    clean_java.set_defaults(func=clean_empty_java)
    clean_java.add_argument("-d", "--daily", action="store_true", help="Keep daily java empty files")
    clean_rust = sub_parser.add_parser("clean_rust", help="Clean error rust files")
    clean_rust.set_defaults(func=clean_error_rust)
    clean_rust.add_argument("-d", "--daily", action="store_true", help="Keep daily rust error files")
    arguments = parser.parse_args()
    arguments.func(arguments)
    sys.exit()
