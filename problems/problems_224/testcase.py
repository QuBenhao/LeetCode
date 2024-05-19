from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input="1 + 1", Output=2))
        self.testcases.append(case(Input=" 2-1 + 2 ", Output=3))
        self.testcases.append(case(Input="(1+(4+5+2)-3)+(6+8)", Output=23))
        self.testcases.append(case(Input="- (3 + (4 + 5))", Output=-12))
        self.testcases.append(case(Input="(7)-(0)+(4)", Output=11))

    def get_testcases(self):
        return self.testcases
