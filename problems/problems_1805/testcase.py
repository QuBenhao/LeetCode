from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input="a123bc34d8ef34", Output=3))
        self.testcases.append(case(Input="leet1234code234", Output=2))
        self.testcases.append(case(Input="a1b01c001", Output=1))

    def get_testcases(self):
        return self.testcases
