from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=(5, [[2, 1], [4, 1]]), Output=2))
        self.testcases.append(case(Input=(6, []), Output=5))
        self.testcases.append(case(Input=(10, [[5, 3], [2, 5], [7, 4], [10, 3]]), Output=5))

    def get_testcases(self):
        return self.testcases
