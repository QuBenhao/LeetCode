from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=([[0, 5], [1, 2], [0, 2], [0, 5], [1, 3]], 5), Output=[0, 2, 0, 0, 0]))
        self.testcases.append(case(Input=([[1, 1], [2, 2], [2, 3]], 4), Output=[1, 1, 0, 0]))

    def get_testcases(self):
        return self.testcases
