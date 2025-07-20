from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(
            case(Input=[[[0, 1, 5], [1, 3, 10], [0, 2, 3], [2, 3, 4]], [True, True, True, True], 10], Output=3))
        self.testcases.append(case(
            Input=[[[0, 1, 7], [1, 4, 5], [0, 2, 6], [2, 3, 6], [3, 4, 2], [2, 4, 6]], [True, True, True, False, True],
                   12], Output=6))
		self.testcases.append(case(Input=[[],[True,True],73], Output=-1))

    def get_testcases(self):
        return self.testcases
