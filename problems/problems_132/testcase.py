from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input="aab", Output=1))
        self.testcases.append(case(Input="a", Output=0))
        self.testcases.append(case(Input="ab", Output=1))
        self.testcases.append(case(Input="leet", Output=2))
        self.testcases.append(case(Input="cdd", Output=1))
        self.testcases.append(case(Input="ccaacabacb", Output=3))
        self.testcases.append(case(Input="coder", Output=4))
        self.testcases.append(case(Input="bb", Output=0))
        self.testcases.append(case(Input="aaaaaabbaaaaaaaaaaaaa",Output=1))
        self.testcases.append(case(Input="abc", Output=2))

    def get_testcases(self):
        return self.testcases
