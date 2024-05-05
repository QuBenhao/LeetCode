import json
import os
import sys
import traceback
from typing import Optional

from dotenv import load_dotenv

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from python.lc_libs import *
from python.constants import constant
from python.utils import get_default_folder, send_text_message


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
                f.writelines([testcase_str, "\n", str(outputs)])
    code_map = get_question_code(slug, lang_slugs=languages)
    if code_map is None:
        return
    for language in languages:
        if language == "python3":
            code = code_map["python3"]
            if code is not None:
                with open(f"{dir_path}/solution.py", "w", encoding="utf-8") as f:
                    f.write(write_solution_python(code))
        else:
            code = code_map[language]
            match language:
                case "golang":
                    with open(f"{dir_path}/solution.go", "w", encoding="utf-8") as f:
                        f.write(write_solution_golang(code, question_id))
                case "java":
                    pass
                case _:
                    break
    print(f"Add question: [{question_id}]{slug}")


def process_daily(problem_folder: str, languages: list[str]):
    daily_info = get_daily_question()
    if not daily_info:
        return 1
    root_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    dir_path = os.path.join(root_path, problem_folder, daily_info['questionId'])
    if not os.path.exists(dir_path):
        os.mkdir(dir_path)
        write_question(dir_path, daily_info['questionId'], daily_info['questionNameEn'], daily_info['questionSlug'], languages)
    else:
        print("solved {} before".format(daily_info['questionId']))
        if languages is not None and any(lang != "python3" for lang in languages):
            if "python3" in languages:
                languages.remove("python3")
            write_question(dir_path, daily_info['questionId'], daily_info['questionNameEn'], daily_info['questionSlug'], languages)
    for lang in languages:
        if lang == "python3":
            continue
        match lang:
            case "golang":
                lines = []
                with open(f"{root_path}/golang/solution_test.go", "r", encoding="utf-8") as f:
                    for line in f.readlines():
                        if "problem \"leetCode/problems/" in line:
                            lines.append("\tproblem \"leetCode/problems/{}\"\n".format(daily_info['questionId']))
                        elif "var problemId string =" in line:
                            lines.append("var problemId string = \"{}\"\n".format(daily_info['questionId']))
                        else:
                            lines.append(line)
                with open(f"{root_path}/golang/solution_test.go", "w", encoding="utf-8") as f:
                    f.writelines(lines)
            case _:
                pass
    with open(f"{root_path}/python/test.py", "r", encoding="utf-8") as f:
        lines = f.readlines()
    with open(f"{root_path}/python/test.py", "w", encoding="utf-8") as f:
        for line in lines:
            if line.startswith("QUESTION ="):
                line = "QUESTION = \"{}\"\n".format(daily_info["questionId"])
            f.write(line)


def process_plans(problem_folder: str, cookie: str):
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
            dir_path = os.path.join(root_path, problem_folder, question_id)
            if not os.path.exists(dir_path):
                os.mkdir(dir_path)
                write_question(dir_path, question_id, info["title"], question_slug)
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
            process_plans(problem_folder, cookie)
    except Exception as e:
        print("Exception caught: ", str(e))
        traceback.print_exc()
        return 1
    return 0


if __name__ == '__main__':
    try:
        load_dotenv()
    except Exception as e:
        print(f"Load Env exception, {e}")
        traceback.print_exc()
    cke = os.getenv(constant.COOKIE)
    pf = os.getenv(constant.PROBLEM_FOLDER, get_default_folder())
    langs = json.loads(os.getenv(constant.LANGUAGES, "[\"python3\"]"))
    exec_res = main(pf, cke, langs)
    sys.exit(exec_res)
