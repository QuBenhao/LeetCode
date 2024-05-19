from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=([3, 3, 2], [1, 2, 3, 2, 1, 2]), Output=[2, 2, 0, 2, 1, 2]))
        self.testcases.append(case(Input=([5, 1, 4, 3, 2], [2, 1, 2, 4, 5, 2, 1]), Output=[1, 4, 1, 4, 1, 3, 2]))

    def get_testcases(self):
        return self.testcases
