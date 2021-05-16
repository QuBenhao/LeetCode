from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=([1], 0), Output=0))
        self.testcases.append(case(Input=([0, 10], 2), Output=6))
        self.testcases.append(case(Input=([1, 3, 6], 3), Output=3))
        self.testcases.append(case(Input=([7, 8, 8], 5), Output=1))
        self.testcases.append(case(Input=([7, 8, 8, 5, 2], 4), Output=5))
        self.testcases.append(case(Input=([3, 1, 10], 4), Output=2))

    def get_testcases(self):
        return self.testcases
