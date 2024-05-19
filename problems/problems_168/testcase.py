from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=1, Output="A"))
        self.testcases.append(case(Input=28, Output="AB"))
        self.testcases.append(case(Input=701, Output="ZY"))
        self.testcases.append(case(Input=2147483647, Output="FXSHRXW"))

    def get_testcases(self):
        return self.testcases
