from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=("daabcbaabcbc", "abc"), Output="dab"))
        self.testcases.append(case(Input=("axxxxyyyyb", "xy"), Output="ab"))

    def get_testcases(self):
        return self.testcases
