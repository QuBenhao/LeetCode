from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=[2, 7, 4, 1, 8, 1], Output=1))
        self.testcases.append(case(Input=[31, 26, 33, 21, 40], Output=5))
        self.testcases.append(case(Input=[1, 2], Output=1))
        self.testcases.append(case(Input=[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 14, 23, 37, 61, 98], Output=1))

    def get_testcases(self):
        return self.testcases
