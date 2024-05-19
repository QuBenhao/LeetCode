from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=([[1, 0], [0, 3]], [0, 1]), Output=True))
        self.testcases.append(case(Input=([[1, 0]], [2, 0]), Output=False))
        self.testcases.append(case(Input=([[2, 0]], [1, 0]), Output=False))
        self.testcases.append(case(Input=([[5, 0], [-10, -2], [0, -5], [-2, -2], [-7, 1]], [7, 7]), Output=False))
        self.testcases.append(case(Input=([[-1, 0], [0, 1], [-1, 0], [0, 1], [-1, 0]], [0, 0]), Output=True))

    def get_testcases(self):
        return self.testcases
