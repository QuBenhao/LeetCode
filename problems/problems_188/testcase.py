from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=(2, [2, 4, 1]), Output=2))
        self.testcases.append(case(Input=(2, [3, 2, 6, 5, 0, 3]), Output=7))

    def get_testcases(self):
        return self.testcases
