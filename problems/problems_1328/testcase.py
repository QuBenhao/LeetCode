from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input="abccba", Output="aaccba"))
        self.testcases.append(case(Input="a", Output=""))
        self.testcases.append(case(Input="aba", Output="abb"))
        self.testcases.append(case(Input="abba", Output="aaba"))

    def get_testcases(self):
        return self.testcases
