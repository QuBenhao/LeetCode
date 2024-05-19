from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3), Output=True))
        self.testcases.append(case(Input=([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13), Output=False))

    def get_testcases(self):
        return self.testcases
