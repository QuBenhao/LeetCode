from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=[1, 2, 3, 2], Output=[1, 2, 3, 3]))
        self.testcases.append(case(Input=[2, 2, 1], Output=[1, 2, 1]))
        self.testcases.append(case(Input=[3, 1, 5, 6, 4, 2], Output=[1, 1, 2, 3, 2, 2]))
        self.testcases.append(case(Input=[5, 3, 4, 4, 4, 2, 1, 1, 4, 1], Output=[1, 1, 2, 3, 4, 1, 1, 2, 5, 3]))

    def get_testcases(self):
        return self.testcases
