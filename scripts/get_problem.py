import argparse
import os
import shutil
import sys
from typing import Optional

from lc_libs import get_question_info, get_questions_by_key_word, get_question_desc, write_problem_md, \
    get_question_testcases, extract_outputs_from_md, write_testcase, get_question_code, write_solution


def main(problem_id: Optional[str], problem_slug: Optional[str], force: bool = False):
    if not problem_id and not problem_slug:
        print("Requires at least one of problem_id or problem_slug to fetch")
        return
    problem_title = None
    if not problem_slug:
        questions = get_questions_by_key_word(problem_id)
        if not questions:
            print(f"Unable to find any questions with problem_id {problem_id}")
            return
        for question in questions:
            if question["paidOnly"]:
                # TODO: need cookie and subscription to get the problem
                continue
            if question["frontendQuestionId"] == problem_id:
                problem_slug = question["titleSlug"]
                problem_title = question["title"]
                break
        if not problem_slug:
            print(f"Unable to find any questions with problem_id {problem_id}, possible questions: {questions}")
            return
    else:
        question_info = get_question_info(problem_slug)
        if not question_info:
            print(f"Unable to check out problem given by slug: {problem_slug}, please check ")
            return
        problem_id = question_info["questionFrontendId"]
        problem_title = question_info["title"]

    root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    dir_path = os.path.join(root_path, "problems", problem_id)
    if os.path.exists(dir_path):
        if not force:
            print(f"Already exists problem [{problem_id}]{problem_slug}")
            return
        shutil.rmtree(dir_path)
    os.mkdir(dir_path)
    desc = get_question_desc(problem_slug)
    if desc is None:
        print(f"Unable to fetch question content, [{problem_id}]{problem_slug}")
        return
    outputs = extract_outputs_from_md(desc)
    print(f"question_id: {problem_id}, outputs: {outputs}")
    testcases = get_question_testcases(problem_slug)
    if testcases is None:
        print(f"Unable to fetch question testcases, [{problem_id}]{problem_slug}")
        return
    code = get_question_code(problem_slug)
    if code is None:
        print(f"Unable to fetch question template code, [{problem_id}]{problem_slug}")
        return
    with open(f"{dir_path}/problem.md", "w") as f:
        f.write(write_problem_md(problem_id, problem_title, desc))
    with open(f"{dir_path}/testcase.py", "w") as f:
        f.write(write_testcase(testcases, outputs))
    with open(f"{dir_path}/solution.py", "w") as f:
        f.write(write_solution(code))
    print(f"Add question: [{problem_id}]{problem_slug}")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-id", "--problem_id", required=False, type=str,
                        help="The problem_frontend_id in LeetCode to fetch.", default=None)
    parser.add_argument("-slug", "--problem_slug", required=False, type=str,
                        help="The problem_slug in LeetCode to fetch.", default=None)
    parser.add_argument("-f", "--force", required=False, action="store_true")
    args = parser.parse_args()
    main(args.problem_id, args.problem_slug, args.force)
    sys.exit()
