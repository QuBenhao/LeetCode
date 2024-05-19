from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=("cacb", "cbba"), Output=5))
        self.testcases.append(case(Input=("ab", "ab"), Output=3))
        self.testcases.append(case(Input=("aa", "bb"), Output=0))

    def get_testcases(self):
        return self.testcases
