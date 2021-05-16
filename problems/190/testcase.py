from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=43261596,Output=964176192))
        self.testcases.append(case(Input=4294967293,Output=3221225471))

    def get_testcases(self):
        return self.testcases
