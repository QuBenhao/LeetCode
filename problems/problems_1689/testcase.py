from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input="32", Output=3))
        self.testcases.append(case(Input="82734", Output=8))
        self.testcases.append(case(Input="27346209830709182346", Output=9))

    def get_testcases(self):
        return self.testcases
