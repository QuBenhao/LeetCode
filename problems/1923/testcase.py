from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=(5, [[0, 1, 2, 3, 4], [2, 3, 4], [4, 0, 1, 2, 3]]), Output=2))
        self.testcases.append(case(Input=(3, [[0], [1], [2]]), Output=0))
        self.testcases.append(case(Input=(5, [[0, 1, 2, 3, 4], [4, 3, 2, 1, 0]]), Output=1))

    def get_testcases(self):
        return self.testcases
