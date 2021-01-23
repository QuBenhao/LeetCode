from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=[3, 1], Output=[1, 2, 3]))
        self.testcases.append(case(Input=[6, 5, 4, 6], Output=[2, 4, 1, 5, 3]))

    def get_testcases(self):
        return self.testcases
