from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input="3+2*2", Output=7))
        self.testcases.append(case(Input=" 3/2 ", Output=1))
        self.testcases.append(case(Input=" 3+5 / 2 ", Output=5))
        self.testcases.append(case(Input="14/3*2 ", Output=8))

    def get_testcases(self):
        return self.testcases
