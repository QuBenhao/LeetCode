from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=([[1, -1, -1], [3, -2, 0]], [1, -1, 0, 1, -1, -1, 3, -2, 0]), Output=True))
        self.testcases.append(case(Input=([[10, -2], [1, 2, 3, 4]], [1, 2, 3, 4, 10, -2]), Output=False))
        self.testcases.append(case(Input=([[1, 2, 3], [3, 4]], [7, 7, 1, 2, 3, 4, 7, 7]), Output=False))

    def get_testcases(self):
        return self.testcases
