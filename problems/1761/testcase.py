from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=(6, [[1, 2], [1, 3], [3, 2], [4, 1], [5, 2], [3, 6]]), Output=3))
        self.testcases.append(
            case(Input=(7, [[1, 3], [4, 1], [4, 3], [2, 5], [5, 6], [6, 7], [7, 5], [2, 6]]), Output=0))

    def get_testcases(self):
        return self.testcases
