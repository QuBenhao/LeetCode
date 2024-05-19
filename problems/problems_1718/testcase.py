from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=3, Output=[3, 1, 2, 3, 2]))
        self.testcases.append(case(Input=5, Output=[5, 3, 1, 4, 3, 5, 2, 4, 2]))

    def get_testcases(self):
        return self.testcases
