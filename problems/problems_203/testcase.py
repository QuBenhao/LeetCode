from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=([1, 2, 6, 3, 4, 5, 6], 6), Output=[1, 2, 3, 4, 5]))
        self.testcases.append(case(Input=([], 1), Output=[]))
        self.testcases.append(case(Input=([7, 7, 7, 7], 7), Output=[]))

    def get_testcases(self):
        return self.testcases
