from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=[-4, -1, 0, 3, 10], Output=[0, 1, 9, 16, 100]))
        self.testcases.append(case(Input=[-7, -3, 2, 3, 11], Output=[4, 9, 9, 49, 121]))

    def get_testcases(self):
        return self.testcases
