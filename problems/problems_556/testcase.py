from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=12, Output=21))
        self.testcases.append(case(Input=21, Output=-1))
        self.testcases.append(case(Input=230241, Output=230412))
        self.testcases.append(case(Input=1999999999, Output=-1))
        self.testcases.append(case(Input=2147483647, Output=-1))

    def get_testcases(self):
        return self.testcases
