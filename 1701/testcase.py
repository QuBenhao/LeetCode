from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=[[1, 2], [2, 5], [4, 3]], Output=5.00000))
        self.testcases.append(case(Input=[[5, 2], [5, 4], [10, 3], [20, 1]], Output=3.25000))

    def get_testcases(self):
        return self.testcases
