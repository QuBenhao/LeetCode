from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=14, Output=[1, 3, 4, 14]))
        self.testcases.append(case(Input=26, Output=[1, 2, 6, 10, 26]))

    def get_testcases(self):
        return self.testcases
