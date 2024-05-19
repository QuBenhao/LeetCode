from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=([1, -1, -2, 4, -7, 3], 2), Output=7))
        self.testcases.append(case(Input=([10, -5, -2, 4, 0, 3], 3), Output=17))
        self.testcases.append(case(Input=([1, -5, -20, 4, -1, 3, -6, -3], 2), Output=0))
        self.testcases.append(case(Input=([1, -1, -2, -3, -7, 3], 3), Output=2))
        self.testcases.append(case(Input=([100, -1, -100, -1, 100], 2), Output=198))
        self.testcases.append(case(Input=([100, -100, -300, -300, -300, -100, 100], 4), Output=0))

    def get_testcases(self):
        return self.testcases
