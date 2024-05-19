from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=([2, 3, 5, 1, 3], 3), Output=[True, True, True, False, True]))
        self.testcases.append(case(Input=([4, 2, 1, 1, 2], 1), Output=[True, False, False, False, False]))
        self.testcases.append(case(Input=([12, 1, 12], 10), Output=[True, False, True]))

    def get_testcases(self):
        return self.testcases
