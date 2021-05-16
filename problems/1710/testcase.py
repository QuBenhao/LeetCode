from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=([[1, 3], [2, 2], [3, 1]], 4), Output=8))
        self.testcases.append(case(Input=([[5, 10], [2, 5], [4, 7], [3, 9]], 10), Output=91))

    def get_testcases(self):
        return self.testcases
