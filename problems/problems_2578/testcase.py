from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=4325, Output=59))
        self.testcases.append(case(Input=687, Output=75))
        self.testcases.append(case(Input=1234, Output=37))
        self.testcases.append(case(Input=10, Output=1))
        self.testcases.append(case(Input=100, Output=1))

    def get_testcases(self):
        return self.testcases
