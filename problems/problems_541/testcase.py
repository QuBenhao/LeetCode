from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=("abcdefg", 2), Output="bacdfeg"))
        self.testcases.append(case(Input=("abcd", 2), Output="bacd"))
        self.testcases.append(case(Input=["abcd",4], Output="dcba"))

    def get_testcases(self):
        return self.testcases
