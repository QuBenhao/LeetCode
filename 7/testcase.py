from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=123, Output=321))
        self.testcases.append(case(Input=-123, Output=-321))
        self.testcases.append(case(Input=120, Output=21))
        self.testcases.append(case(Input=0, Output=0))
        self.testcases.append(case(Input=1534236469, Output=0))
        self.testcases.append(case(Input=-10, Output=-1))
        self.testcases.append(case(Input=-1563847412, Output=0))

    def get_testcases(self):
        return self.testcases
