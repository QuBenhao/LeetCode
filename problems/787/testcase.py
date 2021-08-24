from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=(3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 1), Output=200))
        self.testcases.append(case(Input=(3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 0), Output=500))

    def get_testcases(self):
        return self.testcases
