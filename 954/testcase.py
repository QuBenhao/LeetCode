from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=[3, 1, 3, 6], Output=False))
        self.testcases.append(case(Input=[2, 1, 2, 6], Output=False))
        self.testcases.append(case(Input=[4, -2, 2, -4], Output=True))
        self.testcases.append(case(Input=[1, 2, 4, 16, 8, 4], Output=False))
        self.testcases.append(case(Input=[-5, -3], Output=False))
        self.testcases.append(case(Input=[2, 1, 2, 1, 1, 1, 2, 2], Output=True))

    def get_testcases(self):
        return self.testcases
