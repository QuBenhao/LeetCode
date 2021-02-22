from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input="110", Output=[1, 1, 3]))
        self.testcases.append(case(Input="001011", Output=[11, 8, 5, 4, 3, 4]))

    def get_testcases(self):
        return self.testcases
