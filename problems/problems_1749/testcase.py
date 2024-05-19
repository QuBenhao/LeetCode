from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=[1, -3, 2, 3, -4], Output=5))
        self.testcases.append(case(Input=[2, -5, 1, -4, 3, -2], Output=8))
        self.testcases.append(case(Input=[20, -1, -2, -3, 5], Output=20))

    def get_testcases(self):
        return self.testcases
