from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=[2, 7, 9, 4, 4], Output=10))
        self.testcases.append(case(Input=[1, 2, 3, 4, 5, 100], Output=104))

    def get_testcases(self):
        return self.testcases
