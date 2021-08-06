from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=[[1, 2, 3], [0], [0], [0]], Output=4))
        self.testcases.append(case(Input=[[1], [0, 2, 4], [1, 3, 4], [2], [1, 2]], Output=4))
        self.testcases.append(
            case(Input=[[1, 4], [0, 3, 4, 7, 9], [6, 10], [1, 10], [1, 0], [6], [7, 2, 5], [6, 1, 8], [7], [1], [2, 3]],
                 Output=12))

    def get_testcases(self):
        return self.testcases
