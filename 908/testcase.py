from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=([1], 0), Output=0))
        self.testcases.append(case(Input=([0, 10], 2), Output=6))
        self.testcases.append(case(Input=([1, 3, 6], 3), Output=0))

    def get_testcases(self):
        return self.testcases
