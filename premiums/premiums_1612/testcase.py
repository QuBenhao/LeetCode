from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=[['x'], ['x']], Output=True))
        self.testcases.append(
            case(Input=[["+", "a", "+", None, None, "b", "c"], ["+", "+", "a", "b", "c"]], Output=True))
        self.testcases.append(
            case(Input=[["+", "a", "+", None, None, "b", "c"], ["+", "+", "a", "b", "d"]], Output=False))

    def get_testcases(self):
        return self.testcases
