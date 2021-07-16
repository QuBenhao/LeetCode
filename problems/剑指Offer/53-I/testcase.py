from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=([5, 7, 7, 8, 8, 10], 8), Output=2))
        self.testcases.append(case(Input=([5, 7, 7, 8, 8, 10], 6), Output=0))

    def get_testcases(self):
        return self.testcases
