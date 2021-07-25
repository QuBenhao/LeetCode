from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=([[1, 4], [2, 3], [4, 6]], 1), Output=1))
        self.testcases.append(case(Input=([[3, 10], [1, 5], [2, 6]], 0), Output=2))

    def get_testcases(self):
        return self.testcases
