from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=([1, 7], [3, 4], 10), Output=10))
        self.testcases.append(case(Input=([2, 3], [4, 5, 100], 18), Output=17))
        self.testcases.append(case(Input=([3, 10], [2, 5], 9), Output=8))
        self.testcases.append(case(Input=([10], [1], 1), Output=10))

    def get_testcases(self):
        return self.testcases
