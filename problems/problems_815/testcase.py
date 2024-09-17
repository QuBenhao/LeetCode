from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=([[1, 2, 7], [3, 6, 7]], 1, 6), Output=2))
        self.testcases.append(case(Input=([[7, 12], [4, 5, 15], [6], [15, 19], [9, 12, 13]], 15, 12), Output=-1))
        self.testcases.append(case(Input=[[[1,2,7],[3,6,7]],8,6], Output=-1))

    def get_testcases(self):
        return self.testcases
