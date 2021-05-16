from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input="a1", Output=False))
        self.testcases.append(case(Input="h3", Output=True))
        self.testcases.append(case(Input="c7", Output=False))

    def get_testcases(self):
        return self.testcases
