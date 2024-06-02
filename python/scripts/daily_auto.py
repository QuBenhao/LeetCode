import os
import sys
import traceback
from typing import Optional

from dotenv import load_dotenv

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from python.lc_libs import (get_daily_question, get_question_desc, get_question_testcases, write_problem_md, \
                            write_testcase, extract_outputs_from_md, get_user_study_plans, get_user_study_plan_progress,
                            get_question_info, get_question_code)
import python.lc_libs as lc_libs
from python.constants import constant
from python.utils import get_default_folder, send_text_message


def check_remain_languages(dir_path: str, languages: list[str]) -> list[str]:
    remain_languages = list(languages)
    for _, _, files in os.walk(dir_path):
        for f in files:
            try:
                match f:
                    case "Solution.cpp":
                        remain_languages.remove("cpp")
                    case "solution.go":
                        remain_languages.remove("golang")
                    case "Solution.java":
                        remain_languages.remove("java")
                    case "solution.py":
                        remain_languages.remove("python3")
                    case _:
                        continue
            except ValueError as _:
                continue
        break
    return remain_languages


def write_question(dir_path, question_id: str, question_name: str, slug: str, languages: list[str] = None):
    desc = get_question_desc(slug)
    if desc is not None:
        with open(f"{dir_path}/problem.md", "w", encoding="utf-8") as f:
            f.write(write_problem_md(question_id, question_name, desc))
        testcases, testcase_str = get_question_testcases(slug)
        if testcases is not None:
            outputs = extract_outputs_from_md(desc)
            print(f"question_id: {question_id}, outputs: {outputs}")
            if not languages or "python3" in languages:
                with open(f"{dir_path}/testcase.py", "w", encoding="utf-8") as f:
                    f.write(write_testcase(testcases, outputs))
            with open(f"{dir_path}/testcase", "w", encoding="utf-8") as f:
                f.writelines([testcase_str, "\n",
                              str(outputs).replace("None", "null")
                             .replace("True", "true").replace("False", "false")
                             .replace("'", "\\\"")])
    if not languages:
        return
    code_map = get_question_code(slug, lang_slugs=languages)
    if code_map is None:
        return
    for language in languages:
        code = code_map[language]
        func = getattr(lc_libs, f"write_solution_{language}", None)
        if func is None:
            print("Language not supported yet")
            continue
        match language:
            case "python3":
                main_file = f"{dir_path}/solution.py"
            case "golang":
                main_file = f"{dir_path}/solution.go"
            case "java":
                main_file = f"{dir_path}/Solution.java"
            case "cpp":
                main_file = f"{dir_path}/Solution.cpp"
            case _:
                continue
        with open(main_file, "w", encoding="utf-8") as f:
            f.write(func(code, None, question_id))
    print(f"Add question: [{question_id}]{slug}")


def process_daily(problem_folder: str, languages: list[str]):
    daily_info = get_daily_question()
    if not daily_info:
        return 1
    root_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    dir_path = os.path.join(root_path, problem_folder, f"{problem_folder}_{daily_info['questionId']}")
    if not os.path.exists(dir_path):
        os.mkdir(dir_path)
        write_question(dir_path, daily_info['questionId'], daily_info['questionNameEn'], daily_info['questionSlug'],
                       languages)
    else:
        print("solved {} before".format(daily_info['questionId']))
        remain_languages = check_remain_languages(dir_path, languages)
        write_question(dir_path, daily_info['questionId'], daily_info['questionNameEn'], daily_info['questionSlug'],
                       remain_languages)
    for lang in languages:
        match lang:
            case "python3":
                main_file = f"{root_path}/python/test.py"
            case "golang":
                main_file = f"{root_path}/golang/solution_test.go"
            case "java":
                main_file = f"{root_path}/qubhjava/test/TestMain.java"
            case "cpp":
                main_file = f"{root_path}/WORKSPACE"
            case _:
                print("Language {} is not implemented to save".format(lang))
                continue
        test_func = getattr(lc_libs, f"change_test_{lang}", None)
        if not test_func:
            print("Test function [change_test_{}] not implemented.".format(lang))
            continue
        with open(main_file, "r", encoding="utf-8") as f:
            content = f.read()
        with open(main_file, "w", encoding="utf-8") as f:
            f.write(test_func(content, daily_info['questionId']))


def process_plans(problem_folder: str, cookie: str, languages: list[str] = None):
    plans = get_user_study_plans(cookie)
    if plans is None:
        if not send_text_message("The LeetCode in GitHub secrets might be expired, please check!",
                                 "Currently not be able to load user study plan, skip."):
            print("Unable to send PushDeer notification!")
        print("The LeetCode cookie might be expired, unable to check study plans!")
        return
    problem_ids = []
    for slug in plans:
        plan_prog = get_user_study_plan_progress(slug, cookie)
        print("Plan: {}, total: {}, cur: {}".format(slug, plan_prog["total"], plan_prog["finished"]))
        for question_slug in plan_prog["recommend"]:
            info = get_question_info(question_slug)
            if not info:
                print("Unable to find the question, skip!")
                continue
            question_id = info["questionFrontendId"]
            root_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
            dir_path = os.path.join(root_path, problem_folder, f"{problem_folder}_{question_id}")
            if not os.path.exists(dir_path):
                os.mkdir(dir_path)
                write_question(dir_path, question_id, info["title"], question_slug, languages)
            else:
                remain_languages = check_remain_languages(dir_path, languages)
                write_question(dir_path, question_id, info["title"], question_slug, remain_languages)
            problem_ids.append(question_id)
    if problem_ids:
        root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        with open(f"{root_path}/tests.py", "r", encoding="utf-8") as f:
            lines = f.readlines()
        with open(f"{root_path}/tests.py", "w", encoding="utf-8") as f:
            for line in lines:
                if line.startswith("QUESTIONS ="):
                    line = "QUESTIONS = {}\n".format(problem_ids)
                f.write(line)


def main(problem_folder: str, cookie: Optional[str] = None, languages: list[str] = None):
    try:
        process_daily(problem_folder, languages)
        if cookie is not None and len(cookie) > 0:
            process_plans(problem_folder, cookie, languages)
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
    pf = os.getenv(constant.PROBLEM_FOLDER, get_default_folder())
    try:
        langs = os.getenv(constant.LANGUAGES, "python3").split(",")
    except Exception as _:
        traceback.print_exc()
        langs = ["python3"]
    exec_res = main(pf, cke, langs)
    sys.exit(exec_res)
