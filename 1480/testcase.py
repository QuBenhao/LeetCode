from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=[1, 2, 3, 4], Output=[1, 3, 6, 10]))
        self.testcases.append(case(Input=[1, 1, 1, 1, 1], Output=[1, 2, 3, 4, 5]))
        self.testcases.append(case(Input=[3, 1, 2, 10, 1], Output=[3, 4, 6, 16, 17]))

    def get_testcases(self):
        return self.testcases
