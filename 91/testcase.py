from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input="12", Output=2))
        self.testcases.append(case(Input="226", Output=3))
        self.testcases.append(case(Input="0", Output=0))
        self.testcases.append(case(Input="1", Output=1))
        self.testcases.append(case(Input="27", Output=1))
        self.testcases.append(case(Input="99", Output=1))
        self.testcases.append(case(Input="1201234", Output=3))
        self.testcases.append(case(Input="10", Output=1))
        self.testcases.append(case(Input="2611055971756562", Output=4))

    def get_testcases(self):
        return self.testcases
