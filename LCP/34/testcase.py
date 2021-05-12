from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=([5, 2, 3, 4], 2), Output=12))
        self.testcases.append(case(Input=([4, 1, 3, 9, None, None, 2], 2), Output=16))

    def get_testcases(self):
        return self.testcases
