from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=7, Output=6))
        self.testcases.append(case(Input=14, Output=13))

    def get_testcases(self):
        return self.testcases
