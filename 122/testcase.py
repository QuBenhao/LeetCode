from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=[7, 1, 5, 3, 6, 4], Output=7))
        self.testcases.append(case(Input=[1, 2, 3, 4, 5], Output=4))
        self.testcases.append(case(Input=[7, 6, 4, 3, 1], Output=0))

    def get_testcases(self):
        return self.testcases
