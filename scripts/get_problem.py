import argparse
import os
import random
import shutil
import sys
import time
import traceback
from typing import Optional

from dotenv import load_dotenv

from constants import constant
from lc_libs import get_question_info, get_questions_by_key_word, get_question_desc, write_problem_md, \
    get_question_testcases, extract_outputs_from_md, write_testcase, get_question_code, write_solution
from utils import get_default_folder


def __check_path__(problem_folder: str, problem_id: str, problem_slug: str, force: bool = False, file=None):
    root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    dir_path = os.path.join(root_path, problem_folder, problem_id)
    if os.path.exists(dir_path):
        if not force:
            print(f"Already exists problem [{problem_id}]{problem_slug}", file=file)
            return None
        shutil.rmtree(dir_path)
    os.mkdir(dir_path)
    return dir_path


def process_single_algorithm_problem(problem_folder: str, problem_id: str, problem_slug: str,
                                     problem_title: str, cookie: str, force: bool = False, file=None):
    dir_path = __check_path__(problem_folder, problem_id, problem_slug, force, file)
    if not dir_path:
        return
    desc = get_question_desc(problem_slug, cookie)
    if desc is None:
        print(f"Unable to fetch question content, [{problem_id}]{problem_slug}", file=file)
        return
    code = get_question_code(problem_slug, cookie=cookie)
    if code is None:
        print(f"Unable to fetch question template code, [{problem_id}]{problem_slug}, desc: {desc}", file=file)
        shutil.rmtree(dir_path)
        return
    outputs = extract_outputs_from_md(desc)
    print(f"question_id: {problem_id}, outputs: {outputs}", file=file)
    testcases = get_question_testcases(problem_slug)
    if testcases is None:
        print(f"Unable to fetch question testcases, [{problem_id}]{problem_slug}", file=file)
        return
    with open(f"{dir_path}/problem.md", "w", encoding="utf-8") as f:
        f.write(write_problem_md(problem_id, problem_title, desc))
    with open(f"{dir_path}/testcase.py", "w", encoding="utf-8") as f:
        f.write(write_testcase(testcases, outputs))
    with open(f"{dir_path}/solution.py", "w", encoding="utf-8") as f:
        f.write(write_solution(code))
    print(f"Add question: [{problem_id}]{problem_slug}", file=file)


def process_single_database_problem(problem_folder: str, problem_id: str, problem_slug: str,
                                    problem_title: str, cookie: str, force: bool = False, file=None):
    dir_path = __check_path__(problem_folder, problem_id, problem_slug, force, file)
    if not dir_path:
        return
    desc = get_question_desc(problem_slug, cookie)
    if desc is None:
        print(f"Unable to fetch question content, [{problem_id}]{problem_slug}", file=file)
        return
    with open(f"{dir_path}/problem.md", "w", encoding="utf-8") as f:
        f.write(write_problem_md(problem_id, problem_title, desc))
    code = get_question_code(problem_slug, "mysql", cookie=cookie)
    if code is None:
        print(f"Unable to fetch question template code, [{problem_id}]{problem_slug}, desc: {desc}", file=file)
        shutil.rmtree(dir_path)
        return
    with open(f"{dir_path}/solution.sql", "w", encoding="utf-8") as f:
        f.writelines(code)
    testcases = get_question_testcases(problem_slug, "mysql")
    if testcases is None:
        print(f"Unable to fetch question testcases, [{problem_id}]{problem_slug}", file=file)
        return
    with open(f"{dir_path}/testcase", "w", encoding="utf-8") as f:
        f.writelines("\n".join(testcases))
    print(f"Add question: [{problem_id}]{problem_slug}", file=file)


def main(problem_folder: str, problem_id: Optional[str], problem_slug: Optional[str], problem_category: Optional[str],
         force: bool = False, cookie: Optional[str] = None, fetch_all: bool = False, premium_only: bool = False,
         file: Optional[str] = None):
    if not fetch_all:
        if not problem_id and not problem_slug:
            print("Requires at least one of problem_id or problem_slug to fetch in single mode.")
            return
        if not problem_slug:
            questions = get_questions_by_key_word(problem_id, problem_category) if problem_category \
                else get_questions_by_key_word(problem_id)
            if not questions:
                print(f"Unable to find any questions with problem_id {problem_id}")
                return
            for question in questions:
                if question["paidOnly"] and not cookie:
                    continue
                if question["frontendQuestionId"] == problem_id:
                    problem_slug = question["titleSlug"]
                    break
            if not problem_slug:
                print(f"Unable to find any questions with problem_id {problem_id}, possible questions: {questions}")
                return
        question_info = get_question_info(problem_slug, cookie)
        if not question_info:
            print(f"Unable to check out problem given by slug: {problem_slug}, please check ")
            return
        problem_id = question_info["questionFrontendId"]
        problem_title = question_info["title"]
        pc = question_info["categoryTitle"]
        if str.lower(pc) == "database":
            process_single_database_problem(problem_folder, problem_id, problem_slug, problem_title, cookie, force)
        else:
            process_single_algorithm_problem(problem_folder, problem_id, problem_slug, problem_title, cookie, force)
    else:
        if premium_only and not cookie:
            print("Requires premium cookie to keep going.")
            return
        keyword = None
        if problem_id:
            keyword = problem_id
        if problem_slug:
            keyword = problem_slug
        questions = get_questions_by_key_word(problem_id, problem_category, fetch_all, premium_only) if problem_category \
            else get_questions_by_key_word(problem_id, fetch_all=fetch_all, premium_only=premium_only)
        if not questions:
            print(f"Unable to find any questions with keyword: [{keyword}],"
                  f" fetch_all: [{fetch_all}], premium_only: {premium_only}")
            return
        for question in questions:
            question_info = get_question_info(question["titleSlug"], cookie)
            pc = question_info["categoryTitle"]
            try:
                if file is not None:
                    with open(file, "w", encoding="utf-8") as f:
                        if str.lower(pc) == "database":
                            process_single_database_problem(problem_folder,
                                                            question["frontendQuestionId"], question["titleSlug"],
                                                            question["title"],
                                                            cookie, force, file=f)
                        else:
                            process_single_algorithm_problem(problem_folder,
                                                             question["frontendQuestionId"], question["titleSlug"],
                                                             question["title"],
                                                             cookie, force, file=f)
                else:
                    if str.lower(pc) == "database":
                        process_single_database_problem(problem_folder,
                                                        question["frontendQuestionId"], question["titleSlug"],
                                                        question["title"],
                                                        cookie, force)
                    else:
                        process_single_algorithm_problem(problem_folder,
                                                         question["frontendQuestionId"], question["titleSlug"],
                                                         question["title"],
                                                         cookie, force)
                if premium_only:
                    time.sleep(random.randint(3, 6))
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
    parser.add_argument("-cate", "--problem_category", required=False, type=str,
                        help="The problem category in LeetCode to fetch.", default=None)
    parser.add_argument("-f", "--force", required=False, action="store_true",
                        help="If exists problem before, force will replace it with newly fetched one.")
    parser.add_argument("-all", "--fetch_all", required=False, action="store_true",
                        help="Fetch all questions fitting search conditions from LeetCode.")
    parser.add_argument("-pm", "--premium_only", required=False, action="store_true",
                        help="Only fetch premium questions, need a premium account cookie to execute correctly.")
    parser.add_argument("-debug", "--debug_file", required=False, type=str,
                        help="Debug output file, better debugging when the messages are too long", default=None)
    args = parser.parse_args()

    try:
        load_dotenv()
    except Exception as e:
        print(f"Load Env exception, {e}")
        traceback.print_exc()
    cke = os.getenv(constant.COOKIE)
    pf = os.getenv(constant.PROBLEM_FOLDER, get_default_folder(args.problem_category))

    main(pf, args.problem_id, args.problem_slug, args.problem_category,
         args.force, cke, args.fetch_all, args.premium_only, args.debug_file)
    sys.exit()
