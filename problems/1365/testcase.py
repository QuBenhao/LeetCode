from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=[8, 1, 2, 2, 3], Output=[4, 0, 1, 1, 3]))
        self.testcases.append(case(Input=[6, 5, 4, 8], Output=[2, 1, 0, 3]))
        self.testcases.append(case(Input=[7, 7, 7, 7], Output=[0, 0, 0, 0]))

    def get_testcases(self):
        return self.testcases
