from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=([[1, 2, 4], [3, 4, 3], [2, 3, 1]], 2), Output=7))
        self.testcases.append(case(Input=([[1, 2, 4], [3, 4, 3], [2, 3, 10]], 2), Output=10))
        self.testcases.append(case(Input=([[1, 1, 1], [2, 2, 2], [3, 3, 3], [4, 4, 4]], 3), Output=9))
        self.testcases.append(case(Input=[[[1,3,4],[2,4,1],[1,1,4],[3,5,1],[2,5,5]],3], Output=9))

    def get_testcases(self):
        return self.testcases
