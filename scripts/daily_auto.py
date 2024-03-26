import os
import sys
import traceback
from typing import Optional

from dotenv import load_dotenv
from pypushdeer import PushDeer

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from lc_libs import *
from constants import constant
from utils import get_default_folder


def write_question(dir_path, question_id: str, question_name: str, slug: str):
    desc = get_question_desc(slug)
    if desc is not None:
        with open(f"{dir_path}/problem.md", "w", encoding="utf-8") as f:
            f.write(write_problem_md(question_id, question_name, desc))
        testcases = get_question_testcases(slug)
        if testcases is not None:
            outputs = extract_outputs_from_md(desc)
            print(f"question_id: {question_id}, outputs: {outputs}")
            with open(f"{dir_path}/testcase.py", "w", encoding="utf-8") as f:
                f.write(write_testcase(testcases, outputs))
    code = get_question_code(slug)
    if code is not None:
        with open(f"{dir_path}/solution.py", "w", encoding="utf-8") as f:
            f.write(write_solution(code))
    print(f"Add question: [{question_id}]{slug}")


def process_daily(problem_folder: str):
    daily_info = get_daily_question()
    if not daily_info:
        return 1
    root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    dir_path = os.path.join(root_path, problem_folder, daily_info['questionId'])
    if not os.path.exists(dir_path):
        os.mkdir(dir_path)
        write_question(dir_path, daily_info['questionId'], daily_info['questionNameEn'], daily_info['questionSlug'])
    else:
        print("solved {} before".format(daily_info['questionId']))
    with open(f"{root_path}/test.py", "r", encoding="utf-8") as f:
        lines = f.readlines()
    with open(f"{root_path}/test.py", "w", encoding="utf-8") as f:
        for line in lines:
            if line.startswith("QUESTION ="):
                line = "QUESTION = \"{}\"\n".format(daily_info["questionId"])
            f.write(line)


def process_plans(problem_folder: str, cookie: str, notify_key: str | None):
    plans = get_user_study_plans(cookie)
    if plans is None:
        if notify_key:
            push_deer = PushDeer()
            push_deer.send_text("The LeetCode in GitHub secrets might be expired, please check!",
                                desp="Currently not be able to load user study plan, skip.", pushkey=notify_key)
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
            root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
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


def main(problem_folder: str, cookie: Optional[str] = None, notify_key: Optional[str] = None):
    try:
        process_daily(problem_folder)
        if cookie is not None and len(cookie) > 0:
            process_plans(problem_folder, cookie, notify_key)
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
    push_key = os.getenv(constant.PUSH_KEY)
    pf = os.getenv(constant.PROBLEM_FOLDER, get_default_folder())
    exec_res = main(pf, cke, push_key)
    sys.exit(exec_res)
