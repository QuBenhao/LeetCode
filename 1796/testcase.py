from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input="dfa12321afd", Output=2))
        self.testcases.append(case(Input="abc1111", Output=-1))
        self.testcases.append(case(Input="cx077", Output=0))

    def get_testcases(self):
        return self.testcases
