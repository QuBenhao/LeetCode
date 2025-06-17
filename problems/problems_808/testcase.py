from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=50, Output=0.625))
        self.testcases.append(case(Input=0, Output=0.50000))

    def get_testcases(self):
        return self.testcases
