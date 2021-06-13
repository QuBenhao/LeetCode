from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=([5, 1, 5], 22), Output=0))
        self.testcases.append(case(Input=([3, 4, 1, 2], 25), Output=1))

    def get_testcases(self):
        return self.testcases
