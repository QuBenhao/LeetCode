from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input="23", Output=["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]))
        self.testcases.append(case(Input="", Output=[]))
        self.testcases.append(case(Input="2", Output=["a", "b", "c"]))

    def get_testcases(self):
        return self.testcases
