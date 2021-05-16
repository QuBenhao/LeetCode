from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=([1, 2, 4, 3], 4), Output=1))
        self.testcases.append(case(Input=([1, 2, 2, 1], 2), Output=2))
        self.testcases.append(case(Input=([1, 2, 1, 2], 2), Output=0))
        self.testcases.append(case(Input=([28, 50, 76, 80, 64, 30, 32, 84, 53, 8], 84), Output=4))

    def get_testcases(self):
        return self.testcases
