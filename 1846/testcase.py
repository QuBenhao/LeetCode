from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=[2, 2, 1, 2, 1], Output=2))
        self.testcases.append(case(Input=[100, 1, 1000], Output=3))
        self.testcases.append(case(Input=[1, 2, 3, 4, 5], Output=5))

    def get_testcases(self):
        return self.testcases
