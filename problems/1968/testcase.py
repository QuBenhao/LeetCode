from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=[1, 2, 3, 4, 5], Output=[1, 4, 2, 5, 3]))
        self.testcases.append(case(Input=[6, 2, 0, 9, 7], Output=[0, 7, 2, 9, 6]))

    def get_testcases(self):
        return self.testcases
