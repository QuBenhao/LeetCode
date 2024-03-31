from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=[[2, 1], [3, 4], [3, 2]], Output=[1, 2, 3, 4]))
        self.testcases.append(case(Input=[[4, -2], [1, 4], [-3, 1]], Output=[-2, 4, 1, -3]))
        self.testcases.append(case(Input=[[100000, -100000]], Output=[100000, -100000]))

    def get_testcases(self):
        return self.testcases
