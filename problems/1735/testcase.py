from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=[[2, 6], [5, 1], [73, 660]], Output=[4, 1, 50734910]))
        self.testcases.append(case(Input=[[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]], Output=[1, 2, 3, 10, 5]))

    def get_testcases(self):
        return self.testcases
