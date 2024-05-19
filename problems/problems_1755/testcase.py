from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=([5, -7, 3, 5], 6), Output=0))
        self.testcases.append(case(Input=([7, -9, 15, -2], -5), Output=1))
        self.testcases.append(case(Input=([1, 2, 3], -7), Output=7))

    def get_testcases(self):
        return self.testcases
