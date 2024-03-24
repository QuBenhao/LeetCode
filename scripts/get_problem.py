import argparse
import os
import shutil
import sys
import traceback
from typing import Optional

from dotenv import load_dotenv

from constants import constant
from lc_libs import get_question_info, get_questions_by_key_word, get_question_desc, write_problem_md, \
    get_question_testcases, extract_outputs_from_md, write_testcase, get_question_code, write_solution


def process_single_problem(problem_folder: str, problem_id: str, problem_slug: str, problem_title: str,
                           force: bool = False, file=None):
    root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    dir_path = os.path.join(root_path, problem_folder, problem_id)
    if os.path.exists(dir_path):
        if not force:
            print(f"Already exists problem [{problem_id}]{problem_slug}", file=file)
            return
        shutil.rmtree(dir_path)
    os.mkdir(dir_path)
    desc = get_question_desc(problem_slug)
    if desc is None:
        print(f"Unable to fetch question content, [{problem_id}]{problem_slug}", file=file)
        return
    outputs = extract_outputs_from_md(desc)
    print(f"question_id: {problem_id}, outputs: {outputs}", file=file)
    testcases = get_question_testcases(problem_slug)
    if testcases is None:
        print(f"Unable to fetch question testcases, [{problem_id}]{problem_slug}", file=file)
        return
    code = get_question_code(problem_slug)
    if code is None:
        print(f"Unable to fetch question template code, [{problem_id}]{problem_slug}", file=file)
        return
    with open(f"{dir_path}/problem.md", "w") as f:
        f.write(write_problem_md(problem_id, problem_title, desc))
    with open(f"{dir_path}/testcase.py", "w") as f:
        f.write(write_testcase(testcases, outputs))
    with open(f"{dir_path}/solution.py", "w") as f:
        f.write(write_solution(code))
    print(f"Add question: [{problem_id}]{problem_slug}", file=file)


def main(problem_folder: str, problem_id: Optional[str], problem_slug: Optional[str], force: bool = False,
         cookie: Optional[str] = None, fetch_all: bool = False, premium_only: bool = False, file: Optional[str] = None):
    if not fetch_all:
        if not problem_id and not problem_slug:
            print("Requires at least one of problem_id or problem_slug to fetch in single mode.")
            return
        problem_title = None
        if not problem_slug:
            questions = get_questions_by_key_word(problem_id)
            if not questions:
                print(f"Unable to find any questions with problem_id {problem_id}")
                return
            for question in questions:
                if question["paidOnly"] and not cookie:
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
        process_single_problem(problem_folder, problem_id, problem_slug, problem_title, force)
    else:
        if premium_only and not cookie:
            print("Requires premium cookie to keep going.")
            return
        keyword = None
        if problem_id:
            keyword = problem_id
        if problem_slug:
            keyword = problem_slug
        questions = get_questions_by_key_word(keyword, fetch_all, premium_only)
        if not questions:
            print(f"Unable to find any questions with keyword: [{keyword}],"
                  f" fetch_all: [{fetch_all}], premium_only: {premium_only}")
            return
        for question in questions:
            try:
                process_single_problem(problem_folder,
                                       question["frontendQuestionId"], question["titleSlug"], question["title"],
                                       force, file=file)
            except Exception as e:
                print("Exception caught in problem: [{}]{}, {}".format(
                    question["frontendQuestionId"], question["titleSlug"], e))
                traceback.print_exc()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-id", "--problem_id", required=False, type=str,
                        help="The problem_frontend_id in LeetCode to fetch.", default=None)
    parser.add_argument("-slug", "--problem_slug", required=False, type=str,
                        help="The problem_slug in LeetCode to fetch.", default=None)
    parser.add_argument("-f", "--force", required=False, action="store_true",
                        help="If exists problem before, force will replace it with newly fetched one.")
    parser.add_argument("-all", "--fetch_all", required=False, action="store_true",
                        help="Fetch all questions fitting search conditions from LeetCode.")
    parser.add_argument("-pm", "--premium_only", required=False, action="store_true",
                        help="Only fetch premium questions, need a premium account cookie to execute correctly.")
    parser.add_argument("-debug", "--debug_file", required=False, type=str,
                        help="Debug output file, better debugging when the messages are too long", default=None)
    load_dotenv()
    cke = os.getenv(constant.COOKIE)
    pf = os.getenv(constant.PROBLEM_FOLDER, "problems")

    args = parser.parse_args()
    main(pf, args.problem_id, args.problem_slug, args.force, cke, args.fetch_all, args.premium_only, args.debug_file)
    sys.exit()
