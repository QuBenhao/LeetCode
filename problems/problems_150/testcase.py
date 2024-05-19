from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=['2', '1', '+', '3', '*'], Output=9))
        self.testcases.append(case(Input=['4', '13', '5', '/', '+'], Output=6))
        self.testcases.append(
            case(Input=['10', '6', '9', '3', '+', '-11', '*', '/', '*', '17', '+', '5', '+'], Output=22))
        self.testcases.append(case(Input=["4", "-2", "/", "2", "-3", "-", "-"], Output=-7))

    def get_testcases(self):
        return self.testcases
