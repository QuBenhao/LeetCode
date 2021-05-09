from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=[1,2,3,2], Output=14))
        self.testcases.append(case(Input=[2,3,3,1,2], Output=18))
        self.testcases.append(case(Input=[3,1,5,6,4,2], Output=60))

    def get_testcases(self):
        return self.testcases
