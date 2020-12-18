from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=[1, 2, 3, 4, 5, 6, 7], Output=[1, None, 2, 3, None, 4, 5, 6, 7, None]))

    def get_testcases(self):
        return self.testcases
