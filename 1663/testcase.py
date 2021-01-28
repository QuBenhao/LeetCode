from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=(3, 27), Output="aay"))
        self.testcases.append(case(Input=(5, 73), Output="aaszz"))
        self.testcases.append(case(Input=(5, 130), Output="zzzzz"))

    def get_testcases(self):
        return self.testcases
