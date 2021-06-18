from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input="13", Output="3"))
        self.testcases.append(case(Input="4681", Output="8"))
        self.testcases.append(case(Input="1000000000000000000", Output="999999999999999999"))
        self.testcases.append(case(Input="14919921443713777", Output="496"))

    def get_testcases(self):
        return self.testcases
