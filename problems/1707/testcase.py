from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=([0, 1, 2, 3, 4], [[3, 1], [1, 3], [5, 6]]), Output=[3, 3, 7]))
        self.testcases.append(case(Input=([5, 2, 4, 6, 6, 3], [[12, 4], [8, 1], [6, 3]]), Output=[15, -1, 5]))

    def get_testcases(self):
        return self.testcases
