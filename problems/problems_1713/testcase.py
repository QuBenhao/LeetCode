from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=([5, 1, 3], [9, 4, 2, 3, 4]), Output=2))
        self.testcases.append(case(Input=([6, 4, 8, 1, 3, 2], [4, 7, 6, 2, 3, 8, 6, 1]), Output=3))

    def get_testcases(self):
        return self.testcases
