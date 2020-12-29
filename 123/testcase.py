from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=[3, 3, 5, 0, 0, 3, 1, 4], Output=6))
        self.testcases.append(case(Input=[1, 2, 3, 4, 5], Output=4))
        self.testcases.append(case(Input=[7, 6, 4, 3, 1], Output=0))
        self.testcases.append(case(Input=[1], Output=0))

    def get_testcases(self):
        return self.testcases
