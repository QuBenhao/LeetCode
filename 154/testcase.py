from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=[1, 3, 5], Output=1))
        self.testcases.append(case(Input=[2, 2, 2, 0, 1], Output=0))

    def get_testcases(self):
        return self.testcases
