from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(
            Input=(["PeekingIterator", "next", "peek", "next", "next", "hasNext"], [[[1, 2, 3]], [], [], [], [], []]),
            Output=[None, 1, 2, 2, 3, False]))
        self.testcases.append(case(Input=(
        ["PeekingIterator", "hasNext", "peek", "peek", "next", "next", "peek", "peek", "next", "hasNext", "peek",
         "hasNext", "next", "hasNext"], [[[1, 2, 3, 4]], [], [], [], [], [], [], [], [], [], [], [], [], []]),
                                   Output=[None, True, 1, 1, 1, 2, 3, 3, 3, True, 4, True, 4, False]))

    def get_testcases(self):
        return self.testcases
