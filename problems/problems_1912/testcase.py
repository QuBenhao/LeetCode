from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=(["MovieRentingSystem", "search", "rent", "rent", "report", "drop", "search"],
                                          [[3, [[0, 1, 5], [0, 2, 6], [0, 3, 7], [1, 1, 4], [1, 2, 7], [2, 1, 5]]], [1],
                                           [0, 1], [1, 2], [], [1, 2], [2]]),
                                   Output=[None, [1, 0, 2], None, None, [[0, 1], [1, 2]], None, [0, 1]]))

    def get_testcases(self):
        return self.testcases
