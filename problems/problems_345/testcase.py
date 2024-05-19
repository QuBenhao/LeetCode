from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input="hello", Output="holle"))
        self.testcases.append(case(Input="leetcode", Output="leotcede"))

    def get_testcases(self):
        return self.testcases
