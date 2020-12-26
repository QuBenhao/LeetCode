from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input="000110", Output="111011"))
        self.testcases.append(case(Input="01", Output="01"))

    def get_testcases(self):
        return self.testcases
