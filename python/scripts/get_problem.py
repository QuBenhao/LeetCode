import argparse
import json
import os
import random
import shutil
import sys
import time
import traceback
from typing import Optional
from tqdm import tqdm

from dotenv import load_dotenv

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from python.constants import constant
from python.lc_libs import get_question_info, get_questions_by_key_word, get_question_desc, \
    get_question_testcases, extract_outputs_from_md, get_question_code, \
    get_question_desc_cn, Python3Writer
import python.lc_libs as lc_libs
from python.utils import get_default_folder, back_question_id, format_question_id


def __check_path__(problem_folder: str, problem_id: str, problem_slug: str, force: bool = False,
                   skip_language: bool = False, file=None):
    root_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    dir_path = os.path.join(root_path, problem_folder, f"{problem_folder}_{problem_id}")
    if os.path.exists(dir_path):
        if not force:
            print(f"Already exists problem [{problem_id}]{problem_slug}", file=file)
            return None
        if skip_language:
            return dir_path
        shutil.rmtree(dir_path)
    os.makedirs(dir_path, exist_ok=True)
    return dir_path


def process_single_algorithm_problem(problem_folder: str, problem_id: str, problem_slug: str,
                                     problem_title: str, cookie: str, force: bool = False, skip_language: bool = False,
                                     file=None, languages=None):
    dir_path = __check_path__(problem_folder, problem_id, problem_slug, force, skip_language, file)
    if not dir_path:
        return
    desc = get_question_desc(problem_slug, cookie)
    is_chinese = False
    if desc is None:
        print(f"Unable to fetch question content, [{problem_id}]{problem_slug}", file=file)
        return
    elif "English description is not available for the problem. Please switch to Chinese." in desc:
        desc = ""
        is_chinese = True
    else:
        with open(f"{dir_path}/problem.md", "w", encoding="utf-8") as f:
            f.write(Python3Writer.write_problem_md(problem_id, problem_title, desc))
    cn_result = get_question_desc_cn(problem_slug, cookie=cookie)
    if cn_result is not None:
        cn_desc, cn_title = cn_result
        if is_chinese:
            desc = cn_desc
        with open(f"{dir_path}/problem_zh.md", "w", encoding="utf-8") as f:
            f.write(Python3Writer.write_problem_md(problem_id, cn_title, cn_desc))
    code_maps = get_question_code(problem_slug, lang_slugs=languages, cookie=cookie)
    if code_maps is None:
        print(f"Unable to fetch question template code, [{problem_id}]{problem_slug}, desc: {desc}", file=file)
        shutil.rmtree(dir_path)
        return
    outputs = extract_outputs_from_md(desc, is_chinese)
    print(f"question_id: {problem_id}, outputs: {outputs}", file=file)
    testcases, testcase_str = get_question_testcases(problem_slug)
    if testcases is None:
        print(f"Unable to fetch question testcases, [{problem_id}]{problem_slug}", file=file)
        return
    if not os.path.exists(f"{dir_path}/testcase.py"):
        with open(f"{dir_path}/testcase.py", "w", encoding="utf-8") as f:
            f.write(Python3Writer.write_testcase(testcases, outputs))
    if not os.path.exists(f"{dir_path}/testcase"):
        with open(f"{dir_path}/testcase", "w", encoding="utf-8") as f:
            f.writelines([testcase_str, "\n",
                          str(outputs).replace("None", "null")
                         .replace("True", "true").replace("False", "false")
                         .replace("'", "\"")])
    for key, val in code_maps.items():
        try:
            cls = getattr(lc_libs, f"{key.capitalize()}Writer", None)
            if not cls:
                print(f"Unsupported language {key} yet")
                continue
            obj = cls()
            func = getattr(obj, "write_solution", None)
            if not func:
                print(f"Unsupported language writer {key} yet")
                continue
            solution_file = getattr(obj, "solution_file", None)
            file_path = os.path.join(dir_path, solution_file)
            if skip_language and solution_file and os.path.exists(file_path):
                continue
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(func(val, None, problem_id, problem_folder))
        except Exception as _:
            traceback.print_exc()

    print(f"Add question: [{back_question_id(problem_id)}]{problem_slug}", file=file)


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
        f.write(Python3Writer.write_problem_md(problem_id, problem_title, desc))
    code = get_question_code(problem_slug, ["mysql"], cookie=cookie)["mysql"]
    if code is None:
        print(f"Unable to fetch question template code, [{problem_id}]{problem_slug}, desc: {desc}", file=file)
        shutil.rmtree(dir_path)
        return
    with open(f"{dir_path}/solution.sql", "w", encoding="utf-8") as f:
        f.writelines(code)
    testcases, _ = get_question_testcases(problem_slug, "mysql")
    if testcases is None:
        print(f"Unable to fetch question testcases, [{problem_id}]{problem_slug}", file=file)
        return
    with open(f"{dir_path}/testcase", "w", encoding="utf-8") as f:
        f.writelines("\n".join(testcases))
    print(f"Add question: [{problem_id}]{problem_slug}", file=file)


def main(origin_problem_id: Optional[str], problem_slug: Optional[str], problem_category: Optional[str],
         force: bool = False, cookie: Optional[str] = None, fetch_all: bool = False, premium_only: bool = False,
         file: Optional[str] = None, replace_problem_id: bool = False, skip_language: bool = False,
         languages: list[str] = None, problem_folder: str = None):
    if not fetch_all:
        if not origin_problem_id and not problem_slug:
            print("Requires at least one of problem_id or problem_slug to fetch in single mode.")
            return
        if not problem_slug:
            questions = get_questions_by_key_word(origin_problem_id, problem_category) if problem_category \
                else get_questions_by_key_word(origin_problem_id)
            if not questions:
                print(f"Unable to find any questions with problem_id {origin_problem_id}")
                return
            for question in questions:
                if question["paidOnly"] and not cookie:
                    continue
                if question["frontendQuestionId"] == origin_problem_id:
                    problem_slug = question["titleSlug"]
                    break
            if not problem_slug:
                print(
                    f"Unable to find any questions with problem_id {origin_problem_id}, possible questions: {questions}")
                return
        question_info = get_question_info(problem_slug, cookie)
        if not question_info:
            print(f"Unable to check out problem given by slug: {problem_slug}, please check ")
            return
        problem_id = question_info["questionFrontendId"]
        problem_title = question_info["title"]
        pc = question_info["categoryTitle"]
        paid_only = premium_only or question_info["isPaidOnly"]
        if str.lower(pc) == "database":
            tmp = get_default_folder(pc) if not problem_folder else problem_folder
            process_single_database_problem(tmp, problem_id, problem_slug, problem_title, cookie, force)
        else:
            tmp = get_default_folder(pc, paid_only=paid_only) if not problem_folder else problem_folder
            process_single_algorithm_problem(tmp, problem_id, problem_slug, problem_title, cookie, force,
                                             skip_language, languages=languages)
            if replace_problem_id:
                root_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
                for lang in languages:
                    cls = getattr(lc_libs, f"{lang.capitalize()}Writer", None)
                    if not cls:
                        continue
                    obj = cls()
                    func = getattr(obj, "change_test", None)
                    if not func:
                        continue
                    test_file_path = getattr(obj, "test_file_path", None)
                    if not test_file_path:
                        continue
                    file_path = os.path.join(root_path, test_file_path)
                    with open(file_path, "r", encoding="utf-8") as f:
                        content = f.read()
                    with open(file_path, "w", encoding="utf-8") as f:
                        f.write(func(content, tmp, problem_id))
    else:
        if premium_only and not cookie:
            print("Requires premium cookie to keep going.")
            return
        keyword = None
        if origin_problem_id:
            keyword = origin_problem_id
        if problem_slug:
            keyword = problem_slug
        questions = get_questions_by_key_word(keyword, problem_category, fetch_all, premium_only) if problem_category \
            else get_questions_by_key_word(keyword, fetch_all=fetch_all, premium_only=premium_only)
        if not questions:
            print(f"Unable to find any questions with keyword: [{keyword}],"
                  f" fetch_all: [{fetch_all}], premium_only: {premium_only}")
            return
        for question in tqdm(questions):
            question_info = get_question_info(question["titleSlug"], cookie)
            pc = question_info["categoryTitle"]
            question_id = format_question_id(question["frontendQuestionId"])
            paid_only = premium_only or question_info["isPaidOnly"]
            try:
                if file is not None:
                    with open(file, "w", encoding="utf-8") as f:
                        if str.lower(pc) == "database":
                            tmp = get_default_folder(pc) if not problem_folder else problem_folder
                            process_single_database_problem(tmp, question_id, question["titleSlug"],
                                                            question["title"], cookie, force, file=f)
                        else:
                            tmp = get_default_folder(pc, paid_only=paid_only) if not problem_folder else problem_folder
                            process_single_algorithm_problem(tmp, question_id, question["titleSlug"],
                                                             question["title"], cookie, force, file=f,
                                                             languages=languages)
                else:
                    if str.lower(pc) == "database":
                        tmp = get_default_folder(pc) if not problem_folder else problem_folder
                        process_single_database_problem(tmp, question_id, question["titleSlug"],
                                                        question["title"], cookie, force)
                    else:
                        tmp = get_default_folder(pc, paid_only=paid_only) if not problem_folder else problem_folder
                        process_single_algorithm_problem(tmp, question_id, question["titleSlug"],
                                                         question["title"], cookie, force, languages=languages)
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
    parser.add_argument("-change", "--change_problem_id", required=False, action="store_true",
                        help="Replace the problem id to run in each language.")
    parser.add_argument("-sl", "--skip_language", required=False, action="store_true",
                        help="Skip exist language files in the problem.")
    args = parser.parse_args()

    try:
        load_dotenv()
    except Exception as e:
        print(f"Load Env exception, {e}")
        traceback.print_exc()
    cke = os.getenv(constant.COOKIE)
    pf = os.getenv(constant.PROBLEM_FOLDER, None)
    langs = os.getenv(constant.LANGUAGES, "python3").split(",")
    main(back_question_id(args.problem_id), args.problem_slug, args.problem_category,
         args.force, cke, args.fetch_all, args.premium_only, args.debug_file, args.change_problem_id,
         args.skip_language, langs, problem_folder=pf)
    sys.exit()
