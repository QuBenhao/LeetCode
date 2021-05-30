from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=("99", 9), Output="999"))
        self.testcases.append(case(Input=("-13", 2), Output="-123"))
        self.testcases.append(case(Input=("-132", 3), Output="-1323"))

    def get_testcases(self):
        return self.testcases
