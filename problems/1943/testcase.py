from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=[[1, 4, 5], [4, 7, 7], [1, 7, 9]], Output=[[1, 4, 14], [4, 7, 16]]))
        self.testcases.append(
            case(Input=[[1, 7, 9], [6, 8, 15], [8, 10, 7]], Output=[[1, 6, 9], [6, 7, 24], [7, 8, 15], [8, 10, 7]]))
        self.testcases.append(
            case(Input=[[1, 4, 5], [1, 4, 7], [4, 7, 1], [4, 7, 11]], Output=[[1, 4, 12], [4, 7, 12]]))

    def get_testcases(self):
        return self.testcases
