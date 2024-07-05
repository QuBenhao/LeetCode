import os
import sys
import traceback
from typing import Optional

from dotenv import load_dotenv

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from python.lc_libs import (get_daily_question, get_question_desc, get_question_testcases, Python3Writer,
                            extract_outputs_from_md, get_user_study_plans, get_user_study_plan_progress,
                            get_question_info, get_question_code, get_question_desc_cn)
import python.lc_libs as lc_libs
from python.constants import constant
from python.utils import get_default_folder, send_text_message


def check_remain_languages(dir_path, languages: list[str]) -> list[str]:
    remain_languages = list(languages)
    for _, _, files in os.walk(dir_path):
        for f in files:
            try:
                match f:
                    case lc_libs.CppWriter.solution_file:
                        remain_languages.remove("cpp")
                    case lc_libs.GolangWriter.solution_file:
                        remain_languages.remove("golang")
                    case lc_libs.JavaWriter.solution_file:
                        remain_languages.remove("java")
                    case Python3Writer.solution_file:
                        remain_languages.remove("python3")
                    case lc_libs.TypescriptWriter.solution_file:
                        remain_languages.remove("typescript")
                    case _:
                        continue
            except ValueError as _:
                continue
        break
    return remain_languages


def write_question(dir_path, problem_folder: str, question_id: str, question_name: str,
                   slug: str, languages: list[str] = None, cookie: str = None):
    desc = get_question_desc(slug, cookie)
    cn_result = get_question_desc_cn(slug, cookie)
    cn_desc = None
    if cn_result is not None and cn_result[0] is not None:
        cn_desc, cn_title = cn_result
        with open(f"{dir_path}/problem_zh.md", "w", encoding="utf-8") as f:
            f.write(Python3Writer.write_problem_md(question_id, cn_title, cn_desc))
    if desc is not None:
        is_chinese = False
        if "English description is not available for the problem. Please switch to Chinese." in desc:
            desc = cn_desc if cn_desc else ""
            is_chinese = True
        else:
            with open(f"{dir_path}/problem.md", "w", encoding="utf-8") as f:
                f.write(Python3Writer.write_problem_md(question_id, question_name, desc))
        testcases, testcase_str = get_question_testcases(slug)
        if testcases is not None:
            outputs = extract_outputs_from_md(desc, is_chinese)
            print(f"question_id: {question_id}, outputs: {outputs}")
            if (not languages or "python3" in languages) and not os.path.exists(f"{dir_path}/testcase.py"):
                with open(f"{dir_path}/testcase.py", "w", encoding="utf-8") as f:
                    f.write(Python3Writer.write_testcase(testcases, outputs))
            if not os.path.exists(f"{dir_path}/testcase"):
                with open(f"{dir_path}/testcase", "w", encoding="utf-8") as f:
                    f.writelines([testcase_str, "\n",
                                  str(outputs).replace("None", "null")
                                 .replace("True", "true").replace("False", "false")
                                 .replace("'", "\"")])
    if not languages:
        return
    code_map = get_question_code(slug, lang_slugs=languages, cookie=cookie)
    if code_map is None:
        return
    for language in languages:
        try:
            code = code_map[language]
            cls = getattr(lc_libs, f"{language.capitalize()}Writer", None)
            if not cls:
                print("Language Writer not supported yet")
                continue
            obj = cls()
            func = getattr(obj, f"write_solution", None)
            if func is None:
                print("Language not supported yet")
                continue
            solution_file = getattr(obj, "solution_file", None)
            if not solution_file:
                print("Language solution_file not supported yet")
                continue
            with open(os.path.join(dir_path, solution_file), "w", encoding="utf-8") as f:
                f.write(func(code, None, question_id, problem_folder))
        except Exception as _:
            traceback.print_stack()
            continue
    print(f"Add question: [{question_id}]{slug}")


def process_daily(languages: list[str], problem_folder: str = None):
    daily_info = get_daily_question()
    if not daily_info:
        return 1
    root_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    question_id = daily_info['questionId']
    tmp = get_default_folder(paid_only=daily_info['paidOnly']) if not problem_folder else problem_folder
    dir_path = os.path.join(root_path, tmp, f"{tmp}_{question_id}")
    if not os.path.exists(dir_path):
        os.makedirs(dir_path, exist_ok=True)
        write_question(dir_path, tmp, question_id, daily_info['questionNameEn'], daily_info['questionSlug'],
                       languages)
    else:
        print("solved {} before".format(daily_info['questionId']))
        remain_languages = check_remain_languages(dir_path, languages)
        write_question(dir_path, tmp, question_id, daily_info['questionNameEn'], daily_info['questionSlug'],
                       remain_languages)
    for lang in languages:
        cls = getattr(lc_libs, f"{lang.capitalize()}Writer", None)
        if not cls:
            print("Language Writer not supported yet")
            continue
        obj = cls()
        test_func = getattr(obj, f"change_test", None)
        if not test_func:
            print("Test function [change_test_{}] not implemented.".format(lang))
            continue
        test_file_path = getattr(obj, "test_file_path", None)
        if not test_file_path:
            print("Language {} is not implemented to save".format(lang))
            continue
        file_path = os.path.join(root_path, test_file_path)
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(test_func(content, tmp, question_id))


def process_plans(cookie: str, languages: list[str] = None, problem_folder: str = None):
    plans = get_user_study_plans(cookie)
    if plans is None:
        if not send_text_message("The LeetCode in GitHub secrets might be expired, please check!",
                                 "Currently not be able to load user study plan, skip."):
            print("Unable to send PushDeer notification!")
        print("The LeetCode cookie might be expired, unable to check study plans!")
        return
    problem_ids = []
    root_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    for slug in plans:
        plan_prog = get_user_study_plan_progress(slug, cookie)
        print("Plan: {}, total: {}, cur: {}".format(slug, plan_prog["total"], plan_prog["finished"]))
        for question_slug in plan_prog["recommend"]:
            info = get_question_info(question_slug, cookie)
            if not info:
                print("Unable to find the question, skip!")
                continue
            question_id = info["questionFrontendId"]
            paid_only = info.get("isPaidOnly", False)
            tmp_folder = problem_folder if problem_folder else get_default_folder(paid_only=paid_only)
            dir_path = os.path.join(root_path, tmp_folder, f"{tmp_folder}_{question_id}")
            if not os.path.exists(dir_path):
                os.makedirs(dir_path, exist_ok=True)
                write_question(dir_path, tmp_folder, question_id, info["title"], question_slug, languages, cookie)
            else:
                remain_languages = check_remain_languages(dir_path, languages)
                write_question(dir_path, tmp_folder, question_id, info["title"], question_slug, remain_languages,
                               cookie)
            problem_ids.append([question_id, tmp_folder])
    if problem_ids:
        for lang in languages:
            cls = getattr(lc_libs, f"{lang.capitalize()}Writer", None)
            if not cls:
                print(f"{lang} writer is not supported yet!")
                continue
            obj = cls()
            tests_file_paths = getattr(obj, "tests_file_paths", None)
            if not tests_file_paths:
                print(f"{lang} tests files not exists yet.")
                continue
            tests_func = getattr(obj, "change_tests", None)
            if not tests_func:
                print(f"{lang} run tests not supported yet!")
                continue
            for i, tests_file_path in enumerate(tests_file_paths):
                file_path = os.path.join(root_path, tests_file_path)
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(tests_func(content, problem_ids, i))


def main(problem_folder: str = None, cookie: Optional[str] = None, languages: list[str] = None):
    try:
        process_daily(languages, problem_folder)
        if cookie is not None and len(cookie) > 0:
            process_plans(cookie, languages, problem_folder)
    except Exception as e:
        print("Exception caught: ", str(e))
        traceback.print_exc()
        return 1
    return 0


if __name__ == '__main__':
    rp = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    sys.path.insert(0, os.path.join(rp, "python"))
    try:
        load_dotenv()
    except Exception as e:
        print(f"Load Env exception, {e}")
        traceback.print_exc()
    cke = os.getenv(constant.COOKIE)
    pf = os.getenv(constant.PROBLEM_FOLDER, None)
    try:
        langs_str = os.getenv(constant.LANGUAGES, "python3")
        if not langs_str:
            langs_str = "python3"
        langs = langs_str.split(",")
    except Exception as _:
        traceback.print_exc()
        langs = ["python3"]
    exec_res = main(pf, cke, langs)
    sys.exit(exec_res)
