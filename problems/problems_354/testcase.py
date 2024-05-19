from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=[[5, 4], [6, 4], [6, 7], [2, 3]], Output=3))
        self.testcases.append(case(Input=[[6, 10], [11, 14], [6, 1], [16, 14], [13, 2]], Output=3))
        self.testcases.append(case(Input=[[1, 5], [2, 6], [3, 1], [4, 2], [5, 3],[6, 4]], Output=4))

    def get_testcases(self):
        return self.testcases
