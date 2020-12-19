from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=[9, 9, 6, 0, 6, 6, 9], Output=3))
        self.testcases.append(case(Input=[9, 9, 6, 0, 9, 6, 9], Output=7))

    def get_testcases(self):
        return self.testcases
