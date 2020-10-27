from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=("codeleet", [4, 5, 6, 7, 0, 2, 1, 3]), Output="leetcode"))
        self.testcases.append(case(Input=("abc", [0, 1, 2]), Output="abc"))
        self.testcases.append(case(Input=("aiohn", [3, 1, 4, 2, 0]), Output="nihao"))
        self.testcases.append(case(Input=("aaiougrt", [4, 0, 2, 6, 7, 3, 1, 5]), Output="arigatou"))
        self.testcases.append(case(Input=("art", [1, 0, 2]), Output="rat"))

    def get_testcases(self):
        return self.testcases
