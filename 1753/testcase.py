from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=(2, 4, 6), Output=6))
        self.testcases.append(case(Input=(4, 4, 6), Output=7))
        self.testcases.append(case(Input=(1, 8, 8), Output=8))

    def get_testcases(self):
        return self.testcases
