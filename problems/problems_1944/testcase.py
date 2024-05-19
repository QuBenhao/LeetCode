from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=[10, 6, 8, 5, 11, 9], Output=[3, 1, 2, 1, 1, 0]))
        self.testcases.append(case(Input=[5, 1, 2, 3, 10], Output=[4, 1, 1, 1, 0]))
        self.testcases.append(case(Input=[4, 3, 2, 1], Output=[1, 1, 1, 0]))

    def get_testcases(self):
        return self.testcases
