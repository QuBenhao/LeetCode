from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=[2, 1, 5, 6, 2, 3], Output=10))
        self.testcases.append(case(Input=[1, 2, 3, 4, 5, 6], Output=12))
        self.testcases.append(case(Input=[1, 2, 3, 1, 1, 1], Output=6))
        self.testcases.append(case(Input=[0, 2, 0], Output=2))
        self.testcases.append(case(Input=[], Output=0))
        self.testcases.append(case(Input=[2, 1, 2], Output=3))
        self.testcases.append(case(Input=[4, 2, 0, 3, 2, 5], Output=6))
        self.testcases.append(case(Input=[1], Output=1))

    def get_testcases(self):
        return self.testcases
