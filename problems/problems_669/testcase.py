from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=([1, 0, 2], 1, 2), Output=[1, None, 2]))
        self.testcases.append(case(Input=([3, 0, 4, None, 2, None, None, 1], 1, 3), Output=[3, 2, None, 1]))
        self.testcases.append(case(Input=([1], 1, 2), Output=[1]))
        self.testcases.append(case(Input=([1, None, 2], 1, 3), Output=[1, None, 2]))
        self.testcases.append(case(Input=([1, None, 2], 2, 4), Output=[2]))

    def get_testcases(self):
        return self.testcases
