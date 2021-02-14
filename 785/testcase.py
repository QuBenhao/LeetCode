from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=[[1, 3], [0, 2], [1, 3], [0, 2]], Output=True))
        self.testcases.append(case(Input=[[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]], Output=False))
        self.testcases.append(case(Input=[[4],[],[4],[4],[0,2,3]], Output=True))

    def get_testcases(self):
        return self.testcases
