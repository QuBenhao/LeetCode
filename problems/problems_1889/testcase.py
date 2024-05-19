from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=([2, 3, 5], [[4, 8], [2, 8]]), Output=6))
        self.testcases.append(case(Input=([2, 3, 5], [[1, 4], [2, 3], [3, 4]]), Output=-1))
        self.testcases.append(case(Input=([3, 5, 8, 10, 11, 12], [[12], [11, 9], [10, 5, 14]]), Output=9))

    def get_testcases(self):
        return self.testcases
