from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=([3, 5, 2, 6], 2), Output=[2, 6]))
        self.testcases.append(case(Input=([2, 4, 3, 3, 5, 4, 9, 6], 4), Output=[2, 3, 3, 4]))

    def get_testcases(self):
        return self.testcases
