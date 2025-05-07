import logging
import sys
import os
import json
import argparse

from collections import defaultdict, Counter

sys.path.append(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
)
from python import lc_libs
from python.utils import format_question_id
from python.constants import LOGGING_FORMAT, DATE_FORMAT


def get_args():
    parser = argparse.ArgumentParser(description="Test code snippets for solutions")
    parser.add_argument(
        "-p", "--problem", type=str, help="Problem name to test", default=None
    )
    parser.add_argument("-l", "--lang", type=str, help="Language to test", default=None)
    subparsers = parser.add_subparsers(
        title="subcommands", description="valid subcommands", help="additional help"
    )
    sol = subparsers.add_parser("solution", help="Solution test mode")
    sol.set_defaults(func=test_solution)
    smt = subparsers.add_parser("submit", help="Submit test mode")
    smt.set_defaults(func=test_submit)
    po = subparsers.add_parser("print_origin", help="Print origin code snippets")
    po.set_defaults(func=test_print_origin)
    aqc = subparsers.add_parser("add_question_code", help="Add question code snippets")
    aqc.add_argument("-c", "--cookie", type=str, help="Cookie for premium questions", default=None)
    aqc.set_defaults(func=test_add_question_code)

    return parser.parse_args()


def test_print_origin(args):
    language = args.lang
    problem_id = args.problem
    if not language or not problem_id:
        raise ValueError("Language and problem are required")
    cur_path = os.path.dirname(os.path.abspath(__file__))
    with open(f"{cur_path}/question_code_snippets.json", "r", encoding="utf-8") as f:
        data = json.load(f)
        for problem in data:
            for k, v in problem.items():
                if k != problem_id:
                    continue
                for code in v:
                    if code["langSlug"] != language:
                        continue
                    logging.info(code["code"])
                    return
    logging.warning("No code found for [{}] in [{}]".format(problem_id, language))


def test_add_question_code(args):
    if not args.problem:
        raise ValueError("Problem id is required")
    questions = lc_libs.get_questions_by_key_word(args.problem, "algorithms")
    if not questions:
        raise ValueError(f"Unable to find any questions with problem_id {args.problem}")
    problem_slug = None
    for question in questions:
        if question["paidOnly"] and not args.cookie:
            continue
        if question["frontendQuestionId"] == args.problem:
            problem_slug = question["titleSlug"]
            break
    if problem_slug is None:
        raise ValueError(f"Unable to find problem slug for problem_id {args.problem}")
    code_list = lc_libs.get_question_code_origin(problem_slug, args.cookie)
    if not code_list:
        raise ValueError(f"Unable to find code snippets for problem_id {args.problem} problem {problem_slug}")
    cur_path = os.path.dirname(os.path.abspath(__file__))
    with open(f"{cur_path}/question_code_snippets.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    with open(f"{cur_path}/question_code_snippets.json", "w", encoding="utf-8") as f:
        idx = -1
        for i, problem in enumerate(data):
            if args.problem in problem.keys():
                idx = i
                break
        if idx != -1:
            data[idx] = {args.problem: code_list}
        else:
            data.append({args.problem: code_list})
        json.dump(data, f, indent=4)
        logging.info(f"Code snippets for problem {args.problem} added successfully")


def test_solution(args):
    limit = None
    languages = None
    if args.problem:
        limit = args.problem
    if args.lang:
        languages = set(args.lang.split(","))
    problems = defaultdict(list)
    cur_path = os.path.dirname(os.path.abspath(__file__))
    with open(f"{cur_path}/question_code_snippets.json", "r", encoding="utf-8") as f:
        data = json.load(f)
        for problem in data:
            for k, v in problem.items():
                for code in v:
                    problems[k].append(code)

    code_counter = Counter()
    for test_problem, codes in problems.items():
        if limit and test_problem != limit:
            continue
        print(f"Testing problem {test_problem}")
        for code in codes:
            lang: str = code["langSlug"]
            if languages and lang not in languages:
                continue
            cls = getattr(lc_libs, f"{lang.capitalize()}Writer", None)
            if not cls:
                continue
            obj: lc_libs.LanguageWriter = cls()
            solution_file: str = obj.solution_file
            tmp_sol = solution_file.split(".")
            with open(
                    f"{cur_path}/tmp_{tmp_sol[0]}{code_counter[lang]}.{tmp_sol[1]}",
                    "w",
                    encoding="utf-8",
            ) as f:
                try:
                    f.writelines(obj.write_solution(code["code"], None, format_question_id(test_problem), "problems"))
                    logging.info(f"Code snippet for problem {test_problem} in language {lang} written successfully")
                    code_counter[lang] += 1
                except NotImplementedError as _:
                    f.write(code["code"])
                    logging.warning("Language {} for Problem {} not implemented yet".format(lang, test_problem))
                except Exception as _:
                    logging.error("Language {} for Problem {} error".format(lang, test_problem), exc_info=True)
                    raise
    if not code_counter:
        logging.warning(f"No code snippets found for the given problem [{limit}] and languages [{languages}]")


def test_submit(args):
    if not args.problem:
        raise ValueError("Problem id is required")
    if args.lang:
        languages = args.lang.split(",")
    else:
        languages = ["python3", "golang", "java", "cpp", "typescript", "rust"]
    cur_path = os.path.dirname(os.path.abspath(__file__))
    root_path = os.path.dirname(os.path.dirname(cur_path))
    problem_path = f"{root_path}/problems/problems_{args.problem}/"
    if not os.path.exists(problem_path):
        logging.debug(f"Problem not found in problems folder, checking in premiums folder")
        problem_path = problem_path.replace("problems", "premiums")
        if not os.path.exists(problem_path):
            raise FileNotFoundError(
                f"Problem file not found, check problem: {args.problem}"
            )
        problem_folder = "premiums"
    else:
        problem_folder = "problems"
    for lang in languages:
        cls = getattr(lc_libs, f"{lang.capitalize()}Writer", None)
        if not cls:
            continue
        obj: lc_libs.LanguageWriter = cls()
        solution_file: str = obj.solution_file
        if not solution_file:
            continue
        if not os.path.exists(f"{problem_path}/{solution_file}"):
            logging.warning(f"Solution file not found for {lang} in {problem_path}")
            continue
        code, _ = obj.get_solution_code(root_path, problem_folder, args.problem)
        tmp_sol = solution_file.split(".")
        with open(
                f"{cur_path}/tmp_submit_{tmp_sol[0]}.{tmp_sol[1]}",
                "w",
                encoding="utf-8",
        ) as f:
            f.write(code)
        logging.debug(code)


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, format=LOGGING_FORMAT, datefmt=DATE_FORMAT)
    arguments = get_args()
    arguments.func(arguments)
    sys.exit(0)
