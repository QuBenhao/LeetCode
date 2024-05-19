from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=[4, 2, 5, 3], Output=7))
        self.testcases.append(case(Input=[5, 6, 7, 8], Output=8))
        self.testcases.append(case(Input=[6, 2, 1, 2, 4, 5], Output=10))

    def get_testcases(self):
        return self.testcases
