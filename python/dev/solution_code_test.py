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
    subparsers = parser.add_subparsers(
        title="subcommands", description="valid subcommands", help="additional help"
    )
    sol = subparsers.add_subparsers("solution", type=str, help="Solution test mode")
    sol.set_defaults(func=test_solution)
    smt = subparsers.add_subparsers("submit", type=str, help="Submit test mode")
    smt.set_defaults(func=test_submit)
    parser.add_argument(
        "-p", "--problem", type=str, help="Problem name to test", default=None
    )
    parser.add_argument("-l", "--lang", type=str, help="Language to test", default=None)
    return parser.parse_args()


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
    pass


if __name__ == "__main__":
    args = get_args()
    args.func(args)
    sys.exit(0)
