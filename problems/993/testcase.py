from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=([1, 2, 3, 4], 4, 3), Output=False))
        self.testcases.append(case(Input=([1, 2, 3, None, 4, None, 5], 5, 4), Output=True))
        self.testcases.append(case(Input=([1, 2, 3, None, 4], 2, 3), Output=False))

    def get_testcases(self):
        return self.testcases
