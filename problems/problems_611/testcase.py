from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=[2, 2, 3, 4], Output=3))
        self.testcases.append(case(Input=[4, 2, 3, 4], Output=4))
        self.testcases.append(case(Input=[0, 0, 0], Output=0))
        self.testcases.append(case(Input=[24, 3, 82, 22, 35, 84, 19], Output=10))

    def get_testcases(self):
        return self.testcases
