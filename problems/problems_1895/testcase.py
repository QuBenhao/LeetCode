from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(
            case(Input=[[7, 1, 4, 5, 6], [2, 5, 1, 6, 4], [1, 5, 4, 3, 2], [1, 2, 7, 3, 4]], Output=3))
        self.testcases.append(case(Input=[[5, 1, 3, 1], [9, 3, 3, 1], [1, 3, 3, 8]], Output=2))

    def get_testcases(self):
        return self.testcases
