from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(
            case(Input=([7, 4, 5, 3, 8], [[0, 2, 2], [4, 2, 4], [2, 13, 1000000000]]), Output=[True, False, True]))
        self.testcases.append(
            case(Input=([5, 2, 6, 4, 1], [[3, 1, 2], [4, 10, 3], [3, 10, 100], [4, 100, 30], [1, 3, 1]]),
                 Output=[False, True, True, False, False]))

    def get_testcases(self):
        return self.testcases
