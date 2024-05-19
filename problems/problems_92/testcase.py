from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=[[1, 2, 3, 4, 5], 2, 4], Output=[1, 4, 3, 2, 5]))
        self.testcases.append(case(Input=[[5], 1, 1], Output=[5]))

    def get_testcases(self):
        return self.testcases
