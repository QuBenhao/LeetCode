from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=[10, 2], Output="210"))
        self.testcases.append(case(Input=[3, 30, 34, 5, 9], Output="9534330"))
        self.testcases.append(case(Input=[1], Output="1"))
        self.testcases.append(case(Input=[10], Output="10"))
        self.testcases.append(case(Input=[34323, 3432], Output="343234323"))
        self.testcases.append(case(Input=[0, 0], Output="0"))

    def get_testcases(self):
        return self.testcases
