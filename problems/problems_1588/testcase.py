from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=[1,4,2,5,3], Output=58))
        self.testcases.append(case(Input=[1,2], Output=3))
        self.testcases.append(case(Input=[10,11,12], Output=66))

    def get_testcases(self):
        return self.testcases
