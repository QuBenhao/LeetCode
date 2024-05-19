from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=([1, 2, 3, 4, 5], 2), Output=[4, 5, 1, 2, 3]))
        self.testcases.append(case(Input=([0, 1, 2], 4), Output=[2, 0, 1]))
        self.testcases.append(case(Input=([1], 1), Output=[1]))
        self.testcases.append(case(Input=([1, 2], 3), Output=[2, 1]))

    def get_testcases(self):
        return self.testcases
