import os.path
import sys
import traceback

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from lc_libs import *


def main():
    try:
        daily_info = get_daily_question()
        if not daily_info:
            return 1
        root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        dir_path = os.path.join(root_path, "problems", daily_info['questionId'])
        if not os.path.exists(dir_path):
            os.mkdir(dir_path)
            sg = daily_info['questionSlug']
            desc = get_question_desc(sg)
            if desc is not None:
                with open(f"{dir_path}/problem.md", "w") as f:
                    f.write(write_problem_md(daily_info, desc))
                testcases = get_question_testcases(sg)
                if testcases is not None:
                    outputs = extract_outputs_from_md(desc)
                    with open(f"{dir_path}/testcase.py", "w") as f:
                        f.write(write_testcase(testcases, outputs))
            code = get_question_code(sg)
            if code is not None:
                with open(f"{dir_path}/solution.py", "w") as f:
                    f.write(write_solution(code))
        else:
            print("solved {} before".format(daily_info['questionId']))
        with open(f"{root_path}/test.py", "r") as f:
            lines = f.readlines()
        with open(f"{root_path}/test.py", "w") as f:
            for line in lines:
                if line.startswith("QUESTION ="):
                    line = "QUESTION = \"{}\"\n".format(daily_info["questionId"])
                f.write(line)
    except Exception as e:
        print("Exception caught: ", str(e))
        traceback.print_exc()
        return 1
    return 0


if __name__ == '__main__':
    exec_res = main()
    sys.exit(exec_res)
