from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=([[1, 4], [2, 4], [3, 6], [4, 4]], [2, 3, 4, 5]), Output=[3, 3, 1, 4]))
        self.testcases.append(case(Input=([[2, 3], [2, 5], [1, 8], [20, 25]], [2, 19, 5, 22]), Output=[2, -1, 4, 6]))

    def get_testcases(self):
        return self.testcases
