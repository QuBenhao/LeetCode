import sys
import os
import json
import argparse

from collections import defaultdict, Counter

sys.path.append(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
)
from python import lc_libs


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
                    print(code["code"])
                    return
    print("No code found for [{}] in [{}]".format(problem_id, language))


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
        for code in codes:
            lang: str = code["langSlug"]
            if languages and lang not in languages:
                continue
            cls = getattr(lc_libs, f"{lang.capitalize()}Writer", None)
            if not cls:
                continue
            obj = cls()
            writer_func = getattr(obj, "write_solution", None)
            if not writer_func:
                continue
            solution_file: str = getattr(cls, "solution_file", None)
            if not solution_file:
                continue
            tmp_sol = solution_file.split(".")
            with open(
                f"{cur_path}/tmp_{tmp_sol[0]}{code_counter[lang]}.{tmp_sol[1]}",
                "w",
                encoding="utf-8",
            ) as f:
                f.writelines(writer_func(code["code"], None, test_problem))
                code_counter[lang] += 1


def test_submit(args):
    if not args.problem:
        raise ValueError("Problem id is required")
    if args.lang:
        languages = args.lang.split(",")
    else:
        languages = ["python3", "golang", "java", "cpp", "typescript"]
    cur_path = os.path.dirname(os.path.abspath(__file__))
    root_path = os.path.dirname(os.path.dirname(cur_path))
    problem_path = f"{root_path}/problems/problems_{args.problem}/"
    if not os.path.exists(problem_path):
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
        obj = cls()
        gsc_func = getattr(obj, "get_solution_code", None)
        if not gsc_func:
            continue
        solution_file: str = getattr(cls, "solution_file", None)
        if not solution_file:
            continue
        code, _ = gsc_func(root_path, problem_folder, args.problem)
        tmp_sol = solution_file.split(".")
        with open(
            f"{cur_path}/tmp_submit_{tmp_sol[0]}.{tmp_sol[1]}",
            "w",
            encoding="utf-8",
        ) as f:
            f.write(code)


if __name__ == "__main__":
    args = get_args()
    args.func(args)
    sys.exit(0)
