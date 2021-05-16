from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=[0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], Output=6))

    def get_testcases(self):
        return self.testcases
