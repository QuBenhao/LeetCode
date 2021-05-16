from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input="111000", Output=1))
        self.testcases.append(case(Input="010", Output=0))
        self.testcases.append(case(Input="1110", Output=-1))
        self.testcases.append(case(Input="110", Output=1))
        self.testcases.append(case(Input="001", Output=1))

    def get_testcases(self):
        return self.testcases
