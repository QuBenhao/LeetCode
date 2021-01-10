from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=([1, 2, 3, 4, 5], 2), Output=[1, 4, 3, 2, 5]))
        self.testcases.append(case(Input=([7, 9, 6, 6, 7, 8, 3, 0, 9, 5], 5), Output=[7, 9, 6, 6, 8, 7, 3, 0, 9, 5]))
        self.testcases.append(case(Input=([1], 1), Output=[1]))
        self.testcases.append(case(Input=([1, 2], 1), Output=[2, 1]))
        self.testcases.append(case(Input=([1, 2, 3], 2), Output=[1, 2, 3]))

    def get_testcases(self):
        return self.testcases
