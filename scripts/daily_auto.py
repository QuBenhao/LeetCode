import os.path
import sys
import traceback

from lc_libs import *


def main():
    try:
        daily_info = get_daily_question()
        if not daily_info:
            return 1
        dir_path = "../problems/{}".format(daily_info['questionId'])
        if not os.path.exists(dir_path):
            os.mkdir(dir_path)
            sg = daily_info['questionSlug']
            desc = get_question_desc(sg)
            if desc is not None:
                with open(f"{dir_path}/problem.md", "w") as f:
                    f.write("# {}. {}\n\n{}".format(daily_info['questionId'], daily_info['questionNameEn'], desc))
                testcases = get_question_testcases(sg)
                if testcases is not None:
                    outputs = extract_outputs_from_md(desc)
                    with open(f"{dir_path}/testcase.py", "w") as f:
                        f.write('from collections import namedtuple\n')
                        f.write('import testcase\n\n')
                        f.write('case = namedtuple("Testcase", ["Input", "Output"])\n\n\n')
                        f.write('class Testcase(testcase.Testcase):\n')
                        f.write('\tdef __init__(self):\n')
                        f.write('\t\tself.testcases = []\n')
                        for inputs, outputs in zip(testcases, outputs):
                            f.write(f'\t\tself.testcases.append(case(Input={inputs}, Output={outputs}))\n')
                        f.write('\n\tdef get_testcases(self):\n')
                        f.write('\t\treturn self.testcases\n')
            code = get_question_code(sg)
            if code is not None:
                with open(f"{dir_path}/solution.py", "w") as f:
                    f.write('import solution\n')
                    f.write("from typing import *\n\n\n")
                    f.write(f'class Solution(solution.Solution):\n')
                    f.write('    def solve(self, test_input=None):\n')
                    f.write('        pass\n\n\n')
                    f.write(code)
                    f.write("\n")
        else:
            print("solved before")
        with open(f"../test.py", "r") as f:
            lines = f.readlines()
        with open("../test.py", "w") as f:
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
