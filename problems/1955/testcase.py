from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=[0, 1, 2, 2], Output=3))
        self.testcases.append(case(Input=[2, 2, 0, 0], Output=0))
        self.testcases.append(case(Input=[0, 1, 2, 0, 1, 2], Output=7))

    def get_testcases(self):
        return self.testcases
