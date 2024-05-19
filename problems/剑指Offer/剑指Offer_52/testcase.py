from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=(8, [4, 1, 8, 4, 5], [5, 6, 1, 8, 4, 5], 2, 3), Output=8))
        self.testcases.append(case(Input=(2, [1, 9, 1, 2, 4], [3, 2, 4], 3, 1), Output=2))
        self.testcases.append(case(Input=(0, [2, 6, 4], [1, 5], 3, 2), Output=None))

    def get_testcases(self):
        return self.testcases
