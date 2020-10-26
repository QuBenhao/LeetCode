from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(((2,3),3))
        self.testcases.append(((5,8),5))
        self.testcases.append(((11,13),6))

    def get_testcases(self):
        return self.testcases
