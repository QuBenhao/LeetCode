from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=([1, 2, 3], 1), Output=[1, 0, 2, 1]))
        self.testcases.append(case(Input=([6, 2, 7, 3], 4), Output=[4, 2, 0, 7, 4]))

    def get_testcases(self):
        return self.testcases
