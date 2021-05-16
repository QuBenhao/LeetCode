from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=([1, 2, 0, 3, 0], 1), Output=3))
        self.testcases.append(case(Input=([3, 4, 5, 2, 1, 7, 3, 4, 7], 3), Output=3))
        self.testcases.append(case(Input=([1, 2, 4, 1, 2, 5, 1, 2, 6], 3), Output=3))

    def get_testcases(self):
        return self.testcases
