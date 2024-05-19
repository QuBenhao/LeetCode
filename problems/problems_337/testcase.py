from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=[3, 2, 3, None, 3, None, 1], Output=7))
        self.testcases.append(case(Input=[3, 4, 5, 1, 3, None, 1], Output=9))

    def get_testcases(self):
        return self.testcases
