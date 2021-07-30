from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input="A", Output=1))
        self.testcases.append(case(Input="AB", Output=28))
        self.testcases.append(case(Input="AB", Output=28))
        self.testcases.append(case(Input="ZY", Output=701))
        self.testcases.append(case(Input="FXSHRXW", Output=2147483647))

    def get_testcases(self):
        return self.testcases
