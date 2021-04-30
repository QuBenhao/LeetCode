from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=[2, 2, 3, 2], Output=3))
        self.testcases.append(case(Input=[0, 1, 0, 1, 0, 1, 99], Output=99))
        self.testcases.append(case(Input=[1], Output=1))
        self.testcases.append(case(Input=[30000, 500, 100, 30000, 100, 30000, 100], Output=500))
        self.testcases.append(case(Input=[-2, -2, 1, 1, 4, 1, 4, 4, -4, -2], Output=-4))

    def get_testcases(self):
        return self.testcases
