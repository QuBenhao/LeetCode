from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=[15, 2], Output=7))
        self.testcases.append(case(Input=[7, -3], Output=-2))
        self.testcases.append(case(Input=[-7, 3], Output=-2))
        self.testcases.append(case(Input=[0, 1], Output=0))
        self.testcases.append(case(Input=[1, 1], Output=1))
        self.testcases.append(case(Input=[-2147483648,1], Output=-2147483648))
        self.testcases.append(case(Input=[-2147483648,2], Output=-1073741824))
        self.testcases.append(case(Input=[-2147483648,-1], Output=2147483647))

    def get_testcases(self):
        return self.testcases
