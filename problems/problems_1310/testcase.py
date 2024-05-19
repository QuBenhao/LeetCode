from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=([1, 3, 4, 8], [[0, 1], [1, 2], [0, 3], [3, 3]]), Output=[2, 7, 14, 8]))
        self.testcases.append(case(Input=([4, 8, 2, 10], [[2, 3], [1, 3], [0, 0], [0, 3]]), Output=[8, 0, 4, 4]))

    def get_testcases(self):
        return self.testcases
