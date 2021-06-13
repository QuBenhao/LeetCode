from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=([[2, 5, 3], [1, 8, 4], [1, 7, 5]], [2, 7, 5]), Output=True))
        self.testcases.append(case(Input=([[1, 3, 4], [2, 5, 8]], [2, 5, 8]), Output=True))
        self.testcases.append(case(Input=([[2, 5, 3], [2, 3, 4], [1, 2, 5], [5, 2, 3]], [5, 5, 5]), Output=True))
        self.testcases.append(case(Input=([[3, 4, 5], [4, 5, 6]], [3, 2, 5]), Output=False))

    def get_testcases(self):
        return self.testcases
