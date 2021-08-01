from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=1, Output=8))
        self.testcases.append(case(Input=13, Output=16))
        self.testcases.append(case(Input=1000000000, Output=5040))

    def get_testcases(self):
        return self.testcases
