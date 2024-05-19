from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=([1, 3, 5, 10], 2), Output=2))
        self.testcases.append(case(Input=([3, 6, 8, 10], 3), Output=0))
        self.testcases.append(case(Input=([3, 4, 6, 7], 2), Output=1))
        self.testcases.append(case(Input=([5], 10), Output=0))

    def get_testcases(self):
        return self.testcases
