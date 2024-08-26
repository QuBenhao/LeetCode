import argparse
import logging
import os
import random
import sys

from dotenv import load_dotenv

from daily_auto import write_question

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from python.constants import constant
import python.lc_libs as lc_libs
from python.utils import get_default_folder, format_question_id

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


def lucky(args):
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

    try:
        load_dotenv()
    except Exception as _:
        logging.error("Load Env exception", exc_info=True)
    languages = os.getenv(constant.LANGUAGES, "python3").split(",")
    problem_folder = os.getenv(constant.PROBLEM_FOLDER, get_default_folder())
    category = args.category
    total = lc_libs.get_questions_total(category)
    number = random.randint(1, total)
    logging.info("Random For Problem folder: %s [%d]", problem_folder, number)
    questions = lc_libs.get_questions_by_number(number, category)
    if not questions:
        logging.error(f"No question found for number: {number}")
        return
    central = min(number, 49)
    rpath = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    left = right = central
    while left >= 0 or right < len(questions):
        if right < len(questions):
            if process_problem(rpath, questions[right], languages):
                return
        if left == right:
            left -= 1
            continue
        if left >= 0:
            if process_problem(rpath, questions[left], languages):
                return
        left -= 1
        right += 1
    logging.warning("All problems are solved in random locations, flag: %d", number)


def remain(args):
    try:
        load_dotenv()
    except Exception as _:
        logging.error("Load Env exception", exc_info=True)
    problem_folder = os.getenv(constant.PROBLEM_FOLDER, get_default_folder())
    langs = os.getenv(constant.LANGUAGES, "python3").split(",")
    cookie = os.getenv(constant.COOKIE)
    if not cookie:
        logging.error("Cookie is needed for remaining questions.")
        return
    remains = lc_libs.get_questions_by_status(args.status, args.category, True, cookie=cookie)
    if remains is None:
        logging.error("Failed to get remain problems.")
        return
    if not remains:
        logging.warning("No remain problems found.")
        return
    logging.info("Remain problems: %d", len(remains))
    pick = random.choice(remains)
    question_id = format_question_id(pick["frontendQuestionId"])
    logging.info("Pick problem: [%s].%s", pick["frontendQuestionId"], pick["title"])
    root_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    dir_path = os.path.join(root_path, problem_folder, f"{problem_folder}_{question_id}")
    if os.path.exists(dir_path):
        logging.warning("Folder already exists: %s", dir_path)
        return
    os.makedirs(dir_path, exist_ok=True)
    results = write_question(root_path, dir_path, problem_folder, question_id,
                             pick["title"], pick["titleSlug"], langs)
    logging.info("Problem created: %s", question_id)
    logging.debug("Success languages: %s", results)


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
    arguments = parser.parse_args()
    arguments.func(arguments)
    sys.exit()
