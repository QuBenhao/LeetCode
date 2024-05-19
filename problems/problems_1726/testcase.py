from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=[2, 3, 4, 6], Output=8))
        self.testcases.append(case(Input=[1, 2, 4, 5, 10], Output=16))
        self.testcases.append(case(Input=[2, 3, 4, 6, 8, 12], Output=40))
        self.testcases.append(case(Input=[2, 3, 5, 7], Output=0))

    def get_testcases(self):
        return self.testcases
