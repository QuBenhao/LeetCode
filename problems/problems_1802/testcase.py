from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=(4, 2, 6), Output=2))
        self.testcases.append(case(Input=(6, 1, 10), Output=3))
        self.testcases.append(case(Input=[3,2,18], Output=7))

    def get_testcases(self):
        return self.testcases
