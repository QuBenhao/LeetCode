from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=([1, 7, 5], [2, 3, 5]), Output=3))
        self.testcases.append(case(Input=([2, 4, 6, 8, 10], [2, 4, 6, 8, 10]), Output=0))
        self.testcases.append(case(Input=([1, 10, 4, 4, 2, 7], [9, 3, 5, 1, 7, 4]), Output=20))
        self.testcases.append(case(Input=([95, 1, 2, 3, 4], [100, 2, 3, 4, 5]), Output=8))
        self.testcases.append(case(Input=([10, 11, 7], [1, 7, 3]), Output=13))
        self.testcases.append(case(Input=([8, 7, 6], [6, 1, 8]), Output=8))

    def get_testcases(self):
        return self.testcases
