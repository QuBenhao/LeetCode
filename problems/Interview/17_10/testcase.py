from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=[1, 2, 5, 9, 5, 9, 5, 5, 5], Output=5))
        self.testcases.append(case(Input=[3, 2], Output=-1))
        self.testcases.append(case(Input=[2, 2, 1, 1, 1, 2, 2], Output=2))

    def get_testcases(self):
        return self.testcases
