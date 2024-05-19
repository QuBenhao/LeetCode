from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(
            case(Input=[[3, 4, 5, 1, 3], [3, 3, 4, 2, 3], [20, 30, 200, 40, 10], [1, 5, 5, 4, 1], [4, 3, 2, 2, 5]],
                 Output=[228, 216, 211]))
        self.testcases.append(case(Input=[[1, 2, 3], [4, 5, 6], [7, 8, 9]], Output=[20, 9, 8]))
        self.testcases.append(case(Input=[[7, 7, 7]], Output=[7]))

    def get_testcases(self):
        return self.testcases
