from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input="RLRRLLRLRL", Output=4))
        self.testcases.append(case(Input="RLLLLRRRLR", Output=3))
        self.testcases.append(case(Input="LLLLRRRR", Output=1))
        self.testcases.append(case(Input="RLRRRLLRLL", Output=2))


    def get_testcases(self):
        return self.testcases