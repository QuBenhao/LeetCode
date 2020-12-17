from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(
            case(Input=([1, 0, -1, 0, -2, 2], 0), Output=[[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]))
        self.testcases.append(case(Input=([], 0), Output=[]))
        self.testcases.append(
            case(Input=(
                [-5, 5, 4, -3, 0, 0, 4, -2], 4), Output=[[-5, 0, 4, 5], [-3, -2, 4, 5]]))

    def get_testcases(self):
        return self.testcases
