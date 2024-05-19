from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=(3, [1, 2, 3, 4, 5, 6]), Output=4))
        self.testcases.append(case(Input=(4, [1, 3, 2, 5, 2, 2, 1, 6]), Output=4))

    def get_testcases(self):
        return self.testcases
