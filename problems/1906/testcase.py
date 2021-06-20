from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=([1, 3, 4, 8], [[0, 1], [1, 2], [2, 3], [0, 3]]), Output=[2, 1, 4, 1]))
        self.testcases.append(case(Input=([4, 5, 2, 2, 7, 10], [[2, 3], [0, 2], [0, 5], [3, 5]]), Output=[-1, 1, 1, 3]))

    def get_testcases(self):
        return self.testcases
