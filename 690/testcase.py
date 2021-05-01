from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=([[1, 5, [2, 3]], [2, 3, []], [3, 3, []]], 1), Output=11))

    def get_testcases(self):
        return self.testcases
