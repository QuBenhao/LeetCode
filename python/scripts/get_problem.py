import argparse
import json
import logging
import os
import random
import re
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
                   skip_language: bool = False):
    root_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    dir_path = os.path.join(root_path, problem_folder, f"{problem_folder}_{problem_id}")
    if os.path.exists(dir_path):
        if not force:
            logging.warning(f"Already exists problem [{problem_id}]{problem_slug}")
            return None, None
        if skip_language:
            return root_path, dir_path
        shutil.rmtree(dir_path)
    os.makedirs(dir_path, exist_ok=True)
    return root_path, dir_path


def process_single_algorithm_problem(problem_folder: str, problem_id: str, problem_slug: str,
                                     problem_title: str, cookie: str, force: bool = False, skip_language: bool = False,
                                     languages=None):
    root_path, dir_path = __check_path__(problem_folder, problem_id, problem_slug, force, skip_language)
    if not dir_path:
        return
    desc = get_question_desc(problem_slug, cookie)
    is_chinese = False
    question_rating = lc_libs.get_rating(problem_id)
    if desc is None:
        logging.warning(f"Unable to fetch question content, [{problem_id}]{problem_slug}")
        return
    elif "English description is not available for the problem. Please switch to Chinese." in desc:
        desc = ""
        is_chinese = True
    else:
        with open(f"{dir_path}/problem.md", "w", encoding="utf-8") as f:
            f.write(Python3Writer.write_problem_md(problem_id, problem_title, desc, rating=question_rating))
    cn_result = get_question_desc_cn(problem_slug, cookie=cookie)
    if cn_result is not None:
        cn_desc, cn_title = cn_result
        if is_chinese:
            desc = cn_desc
        with open(f"{dir_path}/problem_zh.md", "w", encoding="utf-8") as f:
            f.write(Python3Writer.write_problem_md(problem_id, cn_title, cn_desc, True, rating=question_rating))
    code_maps = get_question_code(problem_slug, lang_slugs=languages, cookie=cookie)
    if code_maps is None:
        logging.warning(f"Unable to fetch question template code, [{problem_id}]{problem_slug}, desc: {desc}")
        shutil.rmtree(dir_path)
        return
    outputs = extract_outputs_from_md(desc, is_chinese)
    logging.info(f"Load question_id: {problem_id}, test cases outputs: {outputs}")
    testcases, testcase_str = get_question_testcases(problem_slug)
    if not testcases:
        logging.warning(f"Unable to fetch question testcases, [{problem_id}]{problem_slug}")
        # try getting the original question slug
        if "本题与主站" not in desc:
            return
        logging.debug("Try to get the original question slug")
        match = re.search(r"https://(?:leetcode-cn\.com|leetcode\.cn)/problems/(.*?)/\"", desc)
        if not match:
            logging.debug("Failed to get the original question slug, %s", problem_id)
            return
        slug = match.group(1)
        logging.debug(f"Found the original question slug: {slug}")
        testcases, testcase_str = get_question_testcases(slug)
        if not testcases:
            logging.warning(f"Unable to fetch question testcases with origin, [{problem_id}]{problem_slug}")
            return
        logging.info(f"Load question_id from origin question: {slug}, test cases outputs: {testcases}")
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
                logging.warning(f"Unsupported language {key} yet")
                continue
            obj: lc_libs.LanguageWriter = cls()
            solution_file = obj.solution_file
            file_path = os.path.join(dir_path, solution_file)
            if skip_language and solution_file and os.path.exists(file_path):
                continue
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(obj.write_solution(val, None, problem_id, problem_folder))
            if isinstance(obj, lc_libs.RustWriter):
                obj.write_cargo_toml(root_path, dir_path, problem_folder, problem_id)
        except Exception as _:
            logging.error(f"Failed to write [{problem_id}] {key} solution", exc_info=True)

    logging.info(f"Add question: [{back_question_id(problem_id)}]{problem_slug}")


def process_single_database_problem(problem_folder: str, problem_id: str, problem_slug: str,
                                    problem_title: str, cookie: str, force: bool = False):
    _, dir_path = __check_path__(problem_folder, problem_id, problem_slug, force)
    if not dir_path:
        return
    desc = get_question_desc(problem_slug, cookie)
    if desc is None:
        logging.warning(f"Unable to fetch question content, [{problem_id}]{problem_slug}")
        return
    with open(f"{dir_path}/problem.md", "w", encoding="utf-8") as f:
        f.write(Python3Writer.write_problem_md(problem_id, problem_title, desc))
    code = get_question_code(problem_slug, ["mysql"], cookie=cookie)["mysql"]
    if code is None:
        logging.warning(f"Unable to fetch question template code, [{problem_id}]{problem_slug}, desc: {desc}")
        shutil.rmtree(dir_path)
        return
    with open(f"{dir_path}/solution.sql", "w", encoding="utf-8") as f:
        f.writelines(code)
    testcases, _ = get_question_testcases(problem_slug, "mysql")
    if testcases is None:
        logging.warning(f"Unable to fetch question testcases, [{problem_id}]{problem_slug}")
        return
    with open(f"{dir_path}/testcase", "w", encoding="utf-8") as f:
        f.writelines("\n".join(testcases))
    logging.info(f"Add question: [{problem_id}]{problem_slug}")


def get_question_slug_by_id(
        problem_id: str,
        problem_category: Optional[str] = None,
        cookie: Optional[str] = None) -> Optional[str]:
    questions = get_questions_by_key_word(problem_id, problem_category) if problem_category \
        else get_questions_by_key_word(problem_id)
    if not questions:
        logging.error(f"Unable to find any questions with problem_id {problem_id}")
        return None
    for question in questions:
        if question["paidOnly"] and not cookie:
            continue
        if question["frontendQuestionId"] == problem_id:
            return question["titleSlug"]
    logging.error(f"Unable to find any questions with problem_id {problem_id}, possible questions: {questions}")
    return None


def main(origin_problem_id: Optional[str] = None, problem_slug: Optional[str] = None,
         problem_category: Optional[str] = None, force: bool = False, cookie: Optional[str] = None,
         fetch_all: bool = False, premium_only: bool = False, replace_problem_id: bool = False,
         skip_language: bool = False, languages: list[str] = None, problem_folder: str = None):
    if not fetch_all:
        if not origin_problem_id and not problem_slug:
            logging.critical("Requires at least one of problem_id or problem_slug to fetch in single mode.")
            return 1
        if not problem_slug:
            problem_slug = get_question_slug_by_id(origin_problem_id, problem_category, cookie)
            if not problem_slug:
                return 1
        question_info = get_question_info(problem_slug, cookie)
        if not question_info:
            logging.warning(f"Unable to check out problem given by slug: {problem_slug}, please check ")
            return 1
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
                    obj: lc_libs.LanguageWriter = cls()
                    obj.change_test(root_path, tmp, problem_id)
    else:
        if premium_only and not cookie:
            logging.error("Premium problems requires privileged cookie to keep going.")
            return 1
        keyword = None
        if origin_problem_id:
            keyword = origin_problem_id
        if problem_slug:
            keyword = problem_slug
        questions = get_questions_by_key_word(keyword, problem_category, fetch_all, premium_only) if problem_category \
            else get_questions_by_key_word(keyword, fetch_all=fetch_all, premium_only=premium_only)
        if not questions:
            logging.error(f"Unable to find any questions with keyword: [{keyword}],"
                          f" fetch_all: [{fetch_all}], premium_only: {premium_only}")
            return 1
        for question in tqdm(questions):
            question_info = get_question_info(question["titleSlug"], cookie)
            pc = question_info["categoryTitle"]
            question_id = format_question_id(question["frontendQuestionId"])
            paid_only = premium_only or question_info["isPaidOnly"]
            try:
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
            except Exception as _:
                logging.error("Exception caught in problem: [{}]{}".format(
                    question["frontendQuestionId"], question["titleSlug"]), exc_info=True)
                return 1
    return 0


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
    log_level = os.getenv(constant.LOG_LEVEL, "INFO")
    if args.debug_file:
        logging.basicConfig(level=log_level.upper(), format=constant.LOGGING_FORMAT, datefmt=constant.DATE_FORMAT,
                            filename=args.debug_file)
    else:
        logging.basicConfig(level=log_level.upper(), format=constant.LOGGING_FORMAT, datefmt=constant.DATE_FORMAT)
    langs = os.getenv(constant.LANGUAGES, "python3").split(",")
    main(back_question_id(args.problem_id), args.problem_slug, args.problem_category,
         args.force, cke, args.fetch_all, args.premium_only, args.change_problem_id,
         args.skip_language, langs, problem_folder=pf)
    sys.exit()
