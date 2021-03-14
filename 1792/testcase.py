from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=([[1,2],[3,5],[2,2]], 2), Output=0.78333))
        self.testcases.append(case(Input=([[2,4],[3,9],[4,5],[2,10]], 4), Output=0.53485))

    def get_testcases(self):
        return self.testcases
