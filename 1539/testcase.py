from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=([2, 3, 4, 7, 11], 5), Output=9))
        self.testcases.append(case(Input=([1, 2, 3, 4], 2), Output=6))

    def get_testcases(self):
        return self.testcases
