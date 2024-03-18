def write_problem_md(daily_info: dict, desc: str) -> str:
    return "# {}. {}\n\n{}".format(daily_info['questionId'], daily_info['questionNameEn'], desc)


def write_testcase(testcases, outputs) -> str:
    res = ""
    res += 'from collections import namedtuple\n'
    res += 'import testcase\n\n'
    res += 'case = namedtuple("Testcase", ["Input", "Output"])\n\n\n'
    res += 'class Testcase(testcase.Testcase):\n'
    res += '\tdef __init__(self):\n'
    res += '\t\tself.testcases = []\n'
    for inputs, outputs in zip(testcases, outputs):
        res += f'\t\tself.testcases.append(case(Input={inputs}, Output={outputs}))\n'
    res += '\n\tdef get_testcases(self):\n'
    res += '\t\treturn self.testcases\n'
    return res


def write_solution(code: str) -> str:
    return ("import solution\n"
            "from typing import *\n\n\n"
            "class Solution(solution.Solution):\n"
            "    def solve(self, test_input=None):\n"
            "        pass\n\n\n"
            "{}\n").format(code)
