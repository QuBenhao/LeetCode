from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=([1, 3, 2, 8, 4, 9], 2), Output=8))
        self.testcases.append(case(Input=([1, 3, 7, 5, 10, 3], 3), Output=6))

    def get_testcases(self):
        return self.testcases
