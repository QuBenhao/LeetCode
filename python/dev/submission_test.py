import argparse
import os
import sys
import time
import traceback
from typing import Optional

from dotenv import load_dotenv
from pypushdeer import PushDeer

from python.scripts.daily_auto import write_question
from utils import check_problem_solved_python

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from python.lc_libs import check_user_exist, check_accepted_submission, get_submission_detail, \
    write_solution_python, get_user_study_plans, get_user_study_plan_progress, get_question_code, get_question_info, get_questions_by_key_word
from python.constants import constant
from python.utils import get_default_folder


def get_timestamp_days_ago(days):
    # Get today's date
    today = (cur_time := time.time() - time.timezone) - cur_time % 86400 + time.timezone

    # Subtract days
    date_n_days_ago = today - 86400 * days
    # Convert to timestamp (assuming you want a UNIX timestamp)

    return date_n_days_ago


def main(problem_folder: str, user_slug: str, cookie: Optional[str],
         daily_question: str,  days: int,  notify_key: Optional[str] = None):
    try:
        if not check_user_exist(user_slug):
            print(f"User not exist: {user_slug}")
            return 1
        filter_res = get_questions_by_key_word(daily_question)
        for p in filter_res:
            if p["frontendQuestionId"] == daily_question:
                daily_slug = p["titleSlug"]
                break
        else:
            print(f"Daily question {daily_question} not found, {filter_res}")
            return 0
        finish_daily = False
        plan_questions_slug = set()
        finished_plan_questions = []
        if cookie:
            plans = get_user_study_plans(cookie)
            if plans is None:
                if notify_key:
                    push_deer = PushDeer()
                    push_deer.send_text("The LeetCode in GitHub secrets might be expired, please check!",
                                        desp="Currently might not be able to fetch submission.",
                                        pushkey=notify_key)
                print("The LeetCode cookie might be expired!")
            elif plans:
                for plan_slug in plans:
                    plan_prog = get_user_study_plan_progress(plan_slug, cookie, 0)
                    plan_questions_slug = plan_questions_slug.union(plan_prog["all_solved"])
        submit_dict = check_accepted_submission(user_slug, get_timestamp_days_ago(days), get_timestamp_days_ago(days - 1))
        root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        for question_id, submits in submit_dict.items():
            dir_path = os.path.join(root_path, problem_folder, question_id)
            if question_id == daily_question and not os.path.exists(dir_path):
                os.mkdir(dir_path)
                write_question(dir_path, daily_question, "tmp",
                               daily_slug['questionSlug'])
            for submit_id, question_slug in submits:
                if question_id != daily_question and not os.path.exists(dir_path):
                    info = get_question_info(question_slug)
                    os.mkdir(dir_path)
                    write_question(dir_path, question_id, info["title"], question_slug)
                try:
                    check_problem_solved_python(dir_path, question_id, question_slug)
                    if question_id == daily_question:
                        finish_daily = True
                    if question_slug in plan_questions_slug:
                        finished_plan_questions.append(question_slug)
                    break
                except Exception as _:
                    traceback.print_exc()
                detail = get_submission_detail(submit_id, cookie)
                if detail is not None and detail["lang"] == "python3":
                    template = get_question_code(question_slug)["python3"]
                    code = detail["code"]
                    sol_path = os.path.join(str(dir_path), "solution.py")
                    if not os.path.exists(sol_path):
                        if template is not None:
                            with open(f"{dir_path}/solution.py", "w", encoding="utf-8") as f:
                                f.write(write_solution_python(template))
                        else:
                            with open(f"{dir_path}/solution.py", "w", encoding="utf-8") as f:
                                f.write(write_solution_python(code))
                            break
                    with open(f"{dir_path}/solution.py", "r", encoding="utf-8") as f:
                        lines = f.readlines()
                        idx = len(lines) - 1
                        start = False
                        for i, line in enumerate(lines):
                            if "def solve(self, test_input=None):" in line:
                                start = True
                            if start and "return " in line:
                                idx = i
                                break
                        full = "".join(lines[:idx + 1] + ["\n"])
                    with open(f"{dir_path}/solution.py", "w", encoding="utf-8") as f:
                        f.write(full + write_solution_python(template, code))
                    if question_id == daily_question:
                        finish_daily = True
                    break
                elif detail:
                    code = detail["code"]
                    match detail["lang"]:
                        case "java":
                            file_name = "solution.java"
                        case "cpp":
                            file_name = "solution.cpp"
                        case "golang":
                            file_name = "solution.go"
                        case "c":
                            file_name = "solution.c"
                        case "javascript":
                            file_name = "solution.js"
                        case "typescript":
                            file_name = "solution.ts"
                        case _:
                            file_name = "unknown"
                            print("Language {} is not implemented to save".format(detail["lang"]))
                    if not os.path.exists(f"{dir_path}/{file_name}"):
                        with open(f"{dir_path}/{file_name}", "w", encoding="utf-8") as f:
                            f.writelines(code)
                    else:
                        print("Already write [{}] code before".format(detail["lang"]))
                    if question_id == daily_question:
                        finish_daily = True
        print("Daily Question {}: {}, Study plan problem solved today: {}"
              .format(daily_question, "DONE" if finish_daily else "TODO", finished_plan_questions))
        if not finish_daily:
            return 1
    except Exception as e:
        print("Exception caught: ", str(e))
        traceback.print_exc()
        return 1
    return 0


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--user', required=True, type=str, help='The user slug in LeetCode.')
    parser.add_argument("--daily", required=True, type=str, help="The daily problem id of test day.")
    parser.add_argument("--days", required=True, type=int, help="The number of days before.")
    args = parser.parse_args()
    try:
        load_dotenv()
    except Exception as e:
        traceback.print_exc()
    cke = os.getenv(constant.COOKIE)
    push_key = os.getenv(constant.PUSH_KEY)
    pf = os.getenv(constant.PROBLEM_FOLDER, get_default_folder())

    exec_res = main(pf, args.user, cke, args.daily, args.days,push_key)
    sys.exit(exec_res)
