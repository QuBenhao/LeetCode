from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=[1, 2, 3, 4], Output=1))
        self.testcases.append(case(Input=[4, 1, 5, 20, 3], Output=3))
        self.testcases.append(case(Input=[2, 10, 8], Output=3))

    def get_testcases(self):
        return self.testcases
