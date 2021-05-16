from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=[[1993, 1999], [2000, 2010]], Output=1993))
        self.testcases.append(case(Input=[[1950, 1961], [1960, 1971], [1970, 1981]], Output=1960))

    def get_testcases(self):
        return self.testcases
