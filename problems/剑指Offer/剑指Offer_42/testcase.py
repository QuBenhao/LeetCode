from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=[-2, 1, -3, 4, -1, 2, 1, -5, 4], Output=6))

    def get_testcases(self):
        return self.testcases
