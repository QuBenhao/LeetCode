import argparse
import logging
import sys
import os
import traceback
import random
from dotenv import load_dotenv
from daily_auto import write_question

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from python.constants import constant
from python.lc_libs import get_rating, get_questions_total, get_questions_by_number
from python.utils import get_default_folder

PROBLEM_MD = "problem.md"
PROBLEM_MD_ZH = "problem_zh.md"


def back_fill_ratings(args):
    def process_each(dir_path, problem_id: str):
        if not os.path.isdir(dir_path):
            return
        rating = get_rating(problem_id)
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
    except Exception as e:
        print(f"Load Env exception, {e}")
        traceback.print_exc()
    problem_folder = os.getenv(constant.PROBLEM_FOLDER, get_default_folder())
    logging.info("Processing Problem folder: %s", problem_folder)
    if args.problem_id:
        process_each(os.path.join(root_path, problem_folder, f"{problem_folder}_{args.problem_id}"), args.problem_id)
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
        question_id = question["frontendQuestionId"]
        dir_path = os.path.join(root_path, problem_folder, f"{problem_folder}_{question_id}")
        if not os.path.exists(dir_path):
            logging.info("Found: %s", question_id)
            os.makedirs(dir_path, exist_ok=True)
            write_question(dir_path, problem_folder, question_id, question["title"],
                           question["titleSlug"], langs)
            return True
        return False

    try:
        load_dotenv()
    except Exception as e:
        print(f"Load Env exception, {e}")
        traceback.print_exc()
    languages = os.getenv(constant.LANGUAGES, "python3").split(",")
    problem_folder = os.getenv(constant.PROBLEM_FOLDER, get_default_folder())
    category = args.category
    total = get_questions_total(category)
    number = random.randint(1, total)
    logging.info("Random For Problem folder: %s [%d]", problem_folder, number)
    questions = get_questions_by_number(number, category)
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


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format=constant.LOGGING_FORMAT, datefmt=constant.DATE_FORMAT)
    parser = argparse.ArgumentParser()
    sub_parser = parser.add_subparsers()
    bfr = sub_parser.add_parser("rating", help="Back fill ratings")
    bfr.add_argument("-p", "--problem_id", required=False, default=None, help="Add specified Problem id only.")
    bfr.set_defaults(func=back_fill_ratings)
    ly = sub_parser.add_parser("lucky", help="Lucky")
    ly.add_argument("-c", "--category", required=False, default="algorithms", help="Add specified problem category only.")
    ly.set_defaults(func=lucky)
    args = parser.parse_args()
    args.func(args)
    sys.exit()
