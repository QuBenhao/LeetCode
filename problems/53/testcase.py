from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=[-2, 1, -3, 4, -1, 2, 1, -5, 4], Output=6))
        self.testcases.append(case(Input=[1], Output=1))
        self.testcases.append(case(Input=[0], Output=0))
        self.testcases.append(case(Input=[-1], Output=-1))
        self.testcases.append(case(Input=[-2147483647], Output=-2147483647))
        self.testcases.append(case(Input=[-2, -1], Output=-1))
        self.testcases.append(case(Input=[1, 2], Output=3))

    def get_testcases(self):
        return self.testcases
