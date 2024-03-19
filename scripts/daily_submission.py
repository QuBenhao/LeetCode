import os
import sys
import traceback
import argparse
from importlib.util import spec_from_file_location, module_from_spec
from pypushdeer import PushDeer

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from lc_libs import check_user_exist, get_daily_question, check_accepted_submission, get_submission_detail, \
    write_solution, get_user_study_plans, get_user_study_plan_progress


def main(user_slug: str, cookie: str | None, notify_key: str | None = None):
    try:
        if not check_user_exist(user_slug):
            return 1
        daily_info = get_daily_question()
        if not daily_info:
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
        for question_id, (submit_id, question_slug) in submit_dict.items():
            dir_path = os.path.join(root_path, "problems", question_id)
            if os.path.exists(dir_path):
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
                    if question_id == daily_question:
                        finish_daily = True
                    if question_slug in plan_questions_slug:
                        finished_plan_questions.append(question_slug)
                    continue
                except Exception as ex:
                    print("Exception caught: ", str(ex))
                    traceback.print_exc()

                detail = get_submission_detail(submit_id, cookie)
                if detail is not None and detail["lang"] == "python3":
                    code = detail["code"]
                    if not os.path.exists(dir_path):
                        os.mkdir(dir_path)
                    with open(f"{dir_path}/solution.py", "w") as f:
                        f.write(write_solution(code))
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
    parser.add_argument("--notify_key", required=False, type=str,
                        help="The notify key to send notification if any problem occurs.", default=None)
    args = parser.parse_args()
    cke = os.getenv('COOKIE')

    exec_res = main(args.user, cke, args.notify_key)
    sys.exit(exec_res)
