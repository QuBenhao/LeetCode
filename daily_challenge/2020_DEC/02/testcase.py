from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=[1,2,3], Output=None)) # 1,2,3 has the same probability as output

    def get_testcases(self):
        return self.testcases
