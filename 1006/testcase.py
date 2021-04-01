from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=4, Output=7))
        self.testcases.append(case(Input=10, Output=12))

    def get_testcases(self):
        return self.testcases
