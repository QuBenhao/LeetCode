from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=([1, 3, 2], 4, 2), Output=1))
        self.testcases.append(case(Input=([7, 3, 5, 5], 2, 10), Output=2))
        self.testcases.append(case(Input=([7, 3, 5, 5], 1, 10), Output=-1))

    def get_testcases(self):
        return self.testcases
