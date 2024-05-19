from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=[[3, 1, 1], [2, 5, 1], [1, 5, 5], [2, 1, 1]], Output=24))
        self.testcases.append(case(
            Input=[[1, 0, 0, 0, 0, 0, 1], [2, 0, 0, 0, 0, 3, 0], [2, 0, 9, 0, 0, 0, 0], [0, 3, 0, 5, 4, 0, 0],
                   [1, 0, 2, 3, 0, 0, 6]], Output=28))
        self.testcases.append(case(Input=[[1, 0, 0, 3], [0, 0, 0, 3], [0, 0, 3, 3], [9, 0, 3, 3]], Output=22))
        self.testcases.append(case(Input=[[1, 1], [1, 1]], Output=4))
        self.testcases.append(case(Input=[[4, 1, 5, 7, 1], [6, 0, 4, 6, 4], [0, 9, 6, 3, 5]], Output=32))

    def get_testcases(self):
        return self.testcases
