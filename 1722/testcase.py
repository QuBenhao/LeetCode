from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=([1, 2, 3, 4], [2, 1, 4, 5], [[0, 1], [2, 3]]), Output=1))
        self.testcases.append(case(Input=([1, 2, 3, 4], [1, 3, 2, 4], []), Output=2))
        self.testcases.append(
            case(Input=([5, 1, 2, 4, 3], [1, 5, 4, 2, 3], [[0, 4], [4, 2], [1, 3], [1, 4]]), Output=0))

    def get_testcases(self):
        return self.testcases
