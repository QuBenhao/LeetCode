from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=[1, 1, 1], Output=3))
        self.testcases.append(case(Input=[1, 5, 2, 4, 1], Output=14))
        self.testcases.append(case(Input=[8], Output=0))

    def get_testcases(self):
        return self.testcases
