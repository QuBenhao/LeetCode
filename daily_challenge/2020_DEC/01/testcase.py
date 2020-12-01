from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=[3,9,20,None,None,15,7], Output=3))
        self.testcases.append(case(Input=[1,None,2], Output=2))
        self.testcases.append(case(Input=[], Output=0))
        self.testcases.append(case(Input=[0], Output=1))

    def get_testcases(self):
        return self.testcases
