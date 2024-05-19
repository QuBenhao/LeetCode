from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=([1, 4, 2], [1, 2, 4]), Output=2))
        self.testcases.append(case(Input=([2, 5, 1, 2, 5], [10, 5, 2, 1, 5, 2]), Output=3))
        self.testcases.append(case(Input=([1, 3, 7, 1, 7, 5], [1, 9, 2, 5, 1]), Output=2))

    def get_testcases(self):
        return self.testcases
