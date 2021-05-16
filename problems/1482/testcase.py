from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=([1, 10, 3, 10, 2], 3, 1), Output=3))
        self.testcases.append(case(Input=([1, 10, 3, 10, 2], 3, 2), Output=-1))
        self.testcases.append(case(Input=([7, 7, 7, 7, 12, 7, 7], 2, 3), Output=12))
        self.testcases.append(case(Input=([1000000000, 1000000000], 1, 1), Output=1000000000))
        self.testcases.append(case(Input=([1, 10, 2, 9, 3, 8, 4, 7, 5, 6], 4, 2), Output=9))

    def get_testcases(self):
        return self.testcases
