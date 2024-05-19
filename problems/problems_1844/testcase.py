from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input="a1c1e1", Output="abcdef"))
        self.testcases.append(case(Input="a1b2c3d4e", Output="abbdcfdhe"))

    def get_testcases(self):
        return self.testcases
