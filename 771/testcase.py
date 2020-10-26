from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=("aA","aAAbbbb"), Output=3))
        self.testcases.append(case(Input=("z","ZZ"), Output=0))

    def get_testcases(self):
        return self.testcases