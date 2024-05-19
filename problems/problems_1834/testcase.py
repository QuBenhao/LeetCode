from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=[[1, 2], [2, 4], [3, 2], [4, 1]], Output=[0, 2, 3, 1]))
        self.testcases.append(case(Input=[[7, 10], [7, 12], [7, 5], [7, 4], [7, 2]], Output=[4, 3, 2, 0, 1]))

    def get_testcases(self):
        return self.testcases
