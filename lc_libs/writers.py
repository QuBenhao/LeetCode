def write_problem_md(question_id: str, question_name: str, desc: str) -> str:
    return "# {}. {}\n\n{}".format(question_id, question_name, desc)


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
    if "class Solution" or "# class" in code:
        start = False
        strip_start = False
        strip_code = []
        define_class = []
        for line in code.split("\n"):
            if line.startswith("# class"):
                start = True
            if line.startswith("#"):
                if start:
                    define_class.append(line[2:])
                else:
                    if not strip_start:
                        define_class.append(line)
                    else:
                        strip_code.append(line)
                strip_start = False
            else:
                if strip_start:
                    strip_code.append(line)
                if line.startswith("class Solution"):
                    strip_start = True
                start = False
        return ("import solution\n"
                "from typing import *\n\n\n"
                "{}"
                "class Solution(solution.Solution):\n"
                "    def solve(self, test_input=None):\n"
                "        pass\n\n\n"
                "{}").format("\n".join(define_class) + "\n\n\n" if define_class else "", "\n".join(strip_code))
    return ("import solution\n"
            "from typing import *\n\n\n"
            "class Solution(solution.Solution):\n"
            "    def solve(self, test_input=None):\n"
            "        pass\n\n\n"
            "{}\n").format(code)


if __name__ == '__main__':
    print(write_solution(
        "# Definition for a binary tree node.\n# class TreeNode:\n#     def __init__(self, val=0, left=None, right=None):\n#         self.val = val\n#         self.left = left\n#         self.right = right\nclass Solution:\n    def isSymmetric(self, root: Optional[TreeNode]) -> bool:"))
