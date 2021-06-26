from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=[[1, 2, 3], [4, 0, 5]], Output=1))
        self.testcases.append(case(Input=[[1, 2, 3], [5, 4, 0]], Output=-1))
        self.testcases.append(case(Input=[[4, 1, 2], [5, 0, 3]], Output=5))
        self.testcases.append(case(Input=[[3, 2, 4], [1, 5, 0]], Output=14))
        self.testcases.append(case(Input=[[0, 5, 2], [4, 3, 1]], Output=15))

    def get_testcases(self):
        return self.testcases
