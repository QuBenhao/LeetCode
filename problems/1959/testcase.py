from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=([10, 20], 0), Output=10))
        self.testcases.append(case(Input=([10, 20, 30], 1), Output=10))
        self.testcases.append(case(Input=([10, 20, 15, 30, 20], 2), Output=15))

    def get_testcases(self):
        return self.testcases
