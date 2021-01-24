from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=([[5, 2], [1, 6]], 1), Output=7))
        self.testcases.append(case(Input=([[5, 2], [1, 6]], 2), Output=5))
        self.testcases.append(case(Input=([[5, 2], [1, 6]], 3), Output=4))
        self.testcases.append(case(Input=([[5, 2], [1, 6]], 4), Output=0))

    def get_testcases(self):
        return self.testcases
