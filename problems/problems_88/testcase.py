from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3), Output=[1, 2, 2, 3, 5, 6]))
        self.testcases.append(case(Input=([1], 1, [], 0), Output=[1]))
        self.testcases.append(case(Input=([4, 5, 6, 0, 0, 0], 3, [1, 2, 3], 3), Output=[1, 2, 3, 4, 5, 6]))

    def get_testcases(self):
        return self.testcases
