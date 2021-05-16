from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=(["FindSumPairs", "count", "add", "count", "count", "add", "add", "count"],
                                          [[[1, 1, 2, 2, 2, 3], [1, 4, 5, 2, 5, 4]], [7], [3, 2], [8], [4], [0, 1],
                                           [1, 1], [7]]), Output=[None, 8, None, 2, 1, None, None, 11]))

    def get_testcases(self):
        return self.testcases
