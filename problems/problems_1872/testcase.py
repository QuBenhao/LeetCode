from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=[-1, 2, -3, 4, -5], Output=5))
        self.testcases.append(case(Input=[7, -6, 5, 10, 5, -2, -6], Output=13))

    def get_testcases(self):
        return self.testcases
