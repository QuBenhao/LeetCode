from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input="1001", Output=False))
        self.testcases.append(case(Input="110", Output=True))

    def get_testcases(self):
        return self.testcases
