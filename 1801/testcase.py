from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=[[10, 5, 0], [15, 2, 1], [25, 1, 1], [30, 4, 0]], Output=6))
        self.testcases.append(
            case(Input=[[7, 1000000000, 1], [15, 3, 0], [5, 999999995, 0], [5, 1, 1]], Output=999999984))

    def get_testcases(self):
        return self.testcases
