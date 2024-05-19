from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=([-1, 0, 1, 1], [[0, 2], [3, 2], [2, 5]]), Output=[2, 3, 7]))
        self.testcases.append(case(Input=([3, 7, -1, 2, 0, 7, 0, 2], [[4, 6], [1, 15], [0, 5]]), Output=[6, 14, 7]))

    def get_testcases(self):
        return self.testcases
