from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=[1, 2, 3], Output=[1, 2]))
        self.testcases.append(case(Input=[1, 2, 4, 8], Output=[1, 2, 4, 8]))
        self.testcases.append(
            case(Input=[5, 9, 18, 54, 108, 540, 90, 180, 360, 720], Output=[9, 18, 90, 180, 360, 720]))

    def get_testcases(self):
        return self.testcases
