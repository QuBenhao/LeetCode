from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=(5, [[0, 2], [2, 1], [3, 4], [2, 3], [1, 4], [2, 0], [0, 4]], 3), Output=3))
        self.testcases.append(case(Input=(3, [[0, 2], [2, 1]], 2), Output=0))

    def get_testcases(self):
        return self.testcases
