from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input="-1/2+1/2", Output="0/1"))
        self.testcases.append(case(Input="-1/2+1/2+1/3", Output="1/3"))
        self.testcases.append(case(Input="1/3-1/2", Output="-1/6"))
        self.testcases.append(case(Input="5/3+1/3", Output="2/1"))

    def get_testcases(self):
        return self.testcases
