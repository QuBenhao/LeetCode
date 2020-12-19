from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=[6, 0, 8, 2, 1, 5], Output=4))
        self.testcases.append(case(Input=[9, 8, 1, 0, 1, 9, 4, 0, 4, 1], Output=7))

    def get_testcases(self):
        return self.testcases
