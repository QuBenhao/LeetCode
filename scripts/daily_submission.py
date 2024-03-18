import os
import sys
import traceback
import argparse
from importlib.util import spec_from_file_location, module_from_spec

from lc_libs import check_user_exist, get_daily_question, check_accepted_submission, get_submission_detail, \
    write_solution


def main(user_slug: str, cookie: str | None):
    try:
        if not check_user_exist(user_slug):
            return 1
        daily_info = get_daily_question()
        if not daily_info:
            return 1
        question_ids = {daily_info['questionId']}
        submit_dict = check_accepted_submission(user_slug, question_ids)
        for question_id, submit_id in submit_dict.items():
            if os.path.exists(f"../problems/{question_id}"):
                try:
                    testcase_spec = spec_from_file_location("module.name", f"../problems/{question_id}/testcase.py")
                    testcase = module_from_spec(testcase_spec)
                    testcase_spec.loader.exec_module(testcase)
                    testcase_obj = testcase.Testcase()
                    solution_spec = spec_from_file_location("module.name", f"../problems/{question_id}/solution.py")
                    solution = module_from_spec(solution_spec)
                    solution_spec.loader.exec_module(solution)
                    solution_obj = solution.Solution()

                    for test in testcase_obj.get_testcases():
                        i, o = test
                        result = solution_obj.solve(test_input=i)
                        print("Input: {}, Output: {}, Expected: {}".format(i, result, o))
                    if question_id in question_ids:
                        question_ids.remove(question_id)
                    continue
                except Exception as ex:
                    print("Exception caught: ", str(ex))
                    traceback.print_exc()
            if cookie:
                detail = get_submission_detail(submit_id, cookie)
                if detail["lang"] == "python3":
                    code = detail["code"]
                    dir_path = "../problems/{}".format(daily_info['questionId'])
                    if not os.path.exists(dir_path):
                        os.mkdir(dir_path)
                    with open(f"{dir_path}/solution.py", "w") as f:
                        f.write(write_solution(code))
                    if question_id in question_ids:
                        question_ids.remove(question_id)
        if question_ids:
            print("Remain unsolved questions: {}".format(question_ids))
    except Exception as e:
        print("Exception caught: ", str(e))
        traceback.print_exc()
        return 1
    return 0


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--user', required=True, type=str, help='The user slug in LeetCode.')
    parser.add_argument("--cookie", required=False, type=str,
                        help="The user cookie to check submit codes.", default=None)
    args = parser.parse_args()

    exec_res = main(args.user, args.cookie)
    sys.exit(exec_res)
