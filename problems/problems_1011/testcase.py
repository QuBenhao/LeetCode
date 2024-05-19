from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5), Output=15))
        self.testcases.append(case(Input=([3, 2, 2, 4, 1, 4], 3), Output=6))
        self.testcases.append(case(Input=([1, 2, 3, 1, 1], 3), Output=3))
        self.testcases.append(case(Input=([1, 2, 3, 1, 1], 4), Output=3))
        self.testcases.append(case(Input=(
        [180, 373, 75, 82, 497, 23, 303, 299, 53, 426, 152, 314, 206, 433, 283, 370, 179, 254, 265, 431, 453, 17, 189,
         224], 12), Output=631))

    def get_testcases(self):
        return self.testcases
