from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=(2, 3), Output=3))
        self.testcases.append(case(Input=(5, 8), Output=5))
        self.testcases.append(case(Input=(11, 13), Output=6))

    def get_testcases(self):
        return self.testcases
