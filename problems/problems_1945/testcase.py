from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=("iiii", 1), Output=36))
        self.testcases.append(case(Input=("leetcode", 2), Output=6))
        self.testcases.append(case(Input=("zbax", 2), Output=8))

    def get_testcases(self):
        return self.testcases
