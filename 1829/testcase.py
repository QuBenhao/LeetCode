from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=([0, 1, 1, 3], 2), Output=[0, 3, 2, 3]))
        self.testcases.append(case(Input=([2, 3, 4, 7], 3), Output=[5, 2, 6, 5]))
        self.testcases.append(case(Input=([0, 1, 2, 2, 5, 7], 3), Output=[4, 3, 6, 4, 6, 7]))

    def get_testcases(self):
        return self.testcases
