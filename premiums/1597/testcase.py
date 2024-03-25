from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input="3*4-2*5", Output=["-", "*", "*", "3", "4", "2", "5"]))
        self.testcases.append(case(Input="2-3/(5*2)+1",
                                   Output=["+", "-", "1", "2", "/", None, None, None, None, "3", "*", None, None, "5",
                                           "2"]))
        self.testcases.append(
            case(Input="1+2+3+4+5", Output=["+", "+", "5", "+", "4", None, None, "+", "3", None, None, "1", "2"]))

    def get_testcases(self):
        return self.testcases
