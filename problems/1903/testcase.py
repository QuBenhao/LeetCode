from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input="52", Output="5"))
        self.testcases.append(case(Input="4206", Output=""))
        self.testcases.append(case(Input="35427", Output="35427"))

    def get_testcases(self):
        return self.testcases
