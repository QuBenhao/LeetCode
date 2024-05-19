from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(
            case(Input=(["SubrectangleQueries", "getValue", "updateSubrectangle", "getValue", "getValue",
                         "updateSubrectangle", "getValue", "getValue"],
                        [[[[1, 2, 1], [4, 3, 4], [3, 2, 1], [1, 1, 1]]], [0, 2], [0, 0, 3, 2, 5], [0, 2], [3, 1],
                         [3, 0, 3, 2, 10], [3, 1], [0, 2]]),
                 Output=[None, 1, None, 5, 5, None, 10, 5]))
        self.testcases.append(
            case(Input=(
            ["SubrectangleQueries", "getValue", "updateSubrectangle", "getValue", "getValue", "updateSubrectangle",
             "getValue"],
            [[[[1, 1, 1], [2, 2, 2], [3, 3, 3]]], [0, 0], [0, 0, 2, 2, 100], [0, 0], [2, 2], [1, 1, 2, 2, 20], [2, 2]]),
                 Output=[None,1,None,100,100,None,20]))

    def get_testcases(self):
        return self.testcases
