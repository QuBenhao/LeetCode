from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=[3, 4, 5, 1, 2], Output=1))
        self.testcases.append(case(Input=[4, 5, 6, 7, 0, 1, 2], Output=0))
        self.testcases.append(case(Input=[11, 13, 15, 17], Output=11))

    def get_testcases(self):
        return self.testcases
