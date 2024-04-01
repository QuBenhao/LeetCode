import os
import sys
import traceback
import argparse
from importlib.util import spec_from_file_location, module_from_spec
from typing import Optional

from dotenv import load_dotenv
from pypushdeer import PushDeer

from daily_auto import write_question

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from lc_libs import check_user_exist, get_daily_question, check_accepted_submission, get_submission_detail, \
    write_solution, get_user_study_plans, get_user_study_plan_progress, get_question_code, get_question_info
from constants import constant
from utils import get_default_folder


def main(problem_folder: str, user_slug: str, cookie: Optional[str], notify_key: Optional[str] = None):
    try:
        if not check_user_exist(user_slug):
            print(f"User not exist: {user_slug}")
            return 1
        daily_info = get_daily_question()
        if not daily_info:
            print(f"Unable to get daily question")
            return 1
        daily_question = daily_info['questionId']
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
        submit_dict = check_accepted_submission(user_slug)
        root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        for question_id, submits in submit_dict.items():
            dir_path = os.path.join(root_path, problem_folder, question_id)
            if question_id == daily_question and not os.path.exists(dir_path):
                os.mkdir(dir_path)
                write_question(dir_path, daily_question, daily_info['questionNameEn'],
                               daily_info['questionSlug'])
            for submit_id, question_slug in submits:
                if question_id != daily_question and not os.path.exists(dir_path):
                    info = get_question_info(question_slug)
                    os.mkdir(dir_path)
                    write_question(dir_path, question_id, info["title"], question_slug)
                try:
                    testcase_spec = spec_from_file_location("module.name", f"{dir_path}/testcase.py")
                    testcase = module_from_spec(testcase_spec)
                    testcase_spec.loader.exec_module(testcase)
                    testcase_obj = testcase.Testcase()
                    solution_spec = spec_from_file_location("module.name", f"{dir_path}/solution.py")
                    solution = module_from_spec(solution_spec)
                    solution_spec.loader.exec_module(solution)
                    solution_obj = solution.Solution()

                    for test in testcase_obj.get_testcases():
                        i, o = test
                        result = solution_obj.solve(test_input=i)
                        print("Question: [{}]{}, Input: {}, Output: {}, Expected: {}"
                              .format(question_id, question_slug, i, result, o))
                        if o is not None and result is None:
                            raise ValueError("No solution")
                        if o and isinstance(o, list):
                            if o and isinstance(o, list) and isinstance(o[0], float):
                                if any(abs(a - b) > 0.00001 for a, b in zip(o, result)):
                                    raise ValueError("Mismatch float in list")
                            elif all(x is not None for x in o) and isinstance(o[0], list) and not any(
                                    None in x for x in o):
                                if sorted(sorted(item) for item in o) != sorted(sorted(item) for item in result):
                                    raise ValueError("List[List] not equal")
                            else:
                                if None not in o and not (isinstance(o[0], list) and any(None in x for x in o)):
                                    if sorted(o) != sorted(result):
                                        raise ValueError("List not equal")
                                else:
                                    if o != result:
                                        raise ValueError("List Not equal")
                        else:
                            if isinstance(o, float):
                                if abs(o - result) > 0.00001:
                                    raise ValueError("Mismatch float")
                            elif result != o:
                                raise ValueError(f"Result {result} not as expected: {o}")
                    if question_id == daily_question:
                        finish_daily = True
                    if question_slug in plan_questions_slug:
                        finished_plan_questions.append(question_slug)
                    break
                except Exception as ex:
                    print("Exception caught: ", str(ex))
                    traceback.print_exc()
                detail = get_submission_detail(submit_id, cookie)
                if detail is not None and detail["lang"] == "python3":
                    code = detail["code"]
                    sol_path = os.path.join(str(dir_path), "solution.py")
                    if not os.path.exists(sol_path):
                        template = get_question_code(question_slug)
                        if template is not None:
                            with open(f"{dir_path}/solution.py", "w", encoding="utf-8") as f:
                                f.write(write_solution(template))
                        else:
                            with open(f"{dir_path}/solution.py", "w", encoding="utf-8") as f:
                                f.write(write_solution(code, False))
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
                        f.write(full + write_solution(code, False))
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
    args = parser.parse_args()
    try:
        load_dotenv()
    except Exception as e:
        print(f"Load Env exception, {e}")
        traceback.print_exc()
    cke = os.getenv(constant.COOKIE)
    push_key = os.getenv(constant.PUSH_KEY)
    pf = os.getenv(constant.PROBLEM_FOLDER, get_default_folder())

    exec_res = main(pf, args.user, cke, push_key)
    sys.exit(exec_res)
