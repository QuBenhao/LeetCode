from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=(["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"],[[], [1], [2], [], [3], []]),
                                   Output=[None, None, None, 1.5, None, 2.0]))

    def get_testcases(self):
        return self.testcases
