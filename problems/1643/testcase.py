from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=([2, 3], 1), Output="HHHVV"))
        self.testcases.append(case(Input=([2, 3], 2), Output="HHVHV"))
        self.testcases.append(case(Input=([2, 3], 3), Output="HHVVH"))

    def get_testcases(self):
        return self.testcases
