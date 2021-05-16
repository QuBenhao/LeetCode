from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=[1, None, 2, None, 3, None, 4, None, None],
                                   Output=[2, 1, 3, None, None, None, 4] or [3, 1, 4, None, 2, None, None]))

    def get_testcases(self):
        return self.testcases
