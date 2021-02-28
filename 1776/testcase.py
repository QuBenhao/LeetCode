from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(
            case(Input=[[1, 2], [2, 1], [4, 3], [7, 2]], Output=[1.00000, -1.00000, 3.00000, -1.00000]))
        self.testcases.append(
            case(Input=[[3, 4], [5, 4], [6, 3], [9, 1]], Output=[2.00000, 1.00000, 1.50000, -1.00000]))

    def get_testcases(self):
        return self.testcases
