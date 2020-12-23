from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=([4, 1, 2], [1, 3, 4, 2]), Output=[-1, 3, -1]))
        self.testcases.append(case(Input=([2, 4], [1, 2, 3, 4]), Output=[3, -1]))

    def get_testcases(self):
        return self.testcases
