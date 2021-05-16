from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=[[1, 1], 2, [1, 1]], Output=[1, 1, 2, 1, 1]))
        self.testcases.append(case(Input=[1, [4, [6]]], Output=[1, 4, 6]))
        self.testcases.append(
            case(Input=[[], [[]], -4, [[[]]], [[], 2, [[]], [[-3], 1], [[], -1]]], Output=[-4, 2, -3, 1, -1]))

    def get_testcases(self):
        return self.testcases
