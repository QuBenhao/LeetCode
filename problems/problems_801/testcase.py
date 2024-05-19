from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=([1, 3, 5, 4], [1, 2, 3, 7]), Output=1))
        self.testcases.append(case(Input=([3, 3, 8, 9, 10], [1, 7, 4, 6, 8]), Output=1))
        self.testcases.append(case(Input=([0, 4, 4, 5, 9], [0, 1, 6, 8, 10]), Output=1))
        self.testcases.append(
            case(Input=([0, 7, 8, 10, 10, 11, 12, 13, 19, 18], [4, 4, 5, 7, 11, 14, 15, 16, 17, 20]), Output=4))

    def get_testcases(self):
        return self.testcases
