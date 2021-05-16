from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=[-5, 1, 5, 0, -7], Output=1))
        self.testcases.append(case(Input=[-4, -3, -2, -1, 4, 3, 2], Output=0))

    def get_testcases(self):
        return self.testcases
