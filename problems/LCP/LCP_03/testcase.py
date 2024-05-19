from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=("URR", [], 3, 2), Output=True))
        self.testcases.append(case(Input=("URR", [[2, 2]], 3, 2), Output=False))
        self.testcases.append(case(Input=("URR", [[4, 2]], 3, 2), Output=True))
        self.testcases.append(
            case(Input=("RRU", [[5, 5], [9, 4], [9, 7], [6, 4], [7, 0], [9, 5], [10, 7], [1, 1], [7, 5]], 1486, 743),
                 Output=False))
        self.testcases.append(case(Input=("RRRUUU", [[3, 0], [3, 1], [3, 1]], 3, 3), Output=False))

    def get_testcases(self):
        return self.testcases
