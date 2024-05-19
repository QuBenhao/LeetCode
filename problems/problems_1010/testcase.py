from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=[30, 20, 150, 100, 40], Output=3))
        self.testcases.append(case(Input=[60, 60, 60], Output=3))
        self.testcases.append(
            case(Input=[418, 204, 77, 278, 239, 457, 284, 263, 372, 279, 476, 416, 360, 18], Output=1))

    def get_testcases(self):
        return self.testcases
