from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=234, Output=15))
        self.testcases.append(case(Input=4421, Output=21))

    def get_testcases(self):
        return self.testcases