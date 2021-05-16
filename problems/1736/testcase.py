from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input="2?:?0", Output="23:50"))
        self.testcases.append(case(Input="0?:3?", Output="09:39"))
        self.testcases.append(case(Input="1?:22", Output="19:22"))

    def get_testcases(self):
        return self.testcases
