from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=("bank", "kanb"), Output=True))
        self.testcases.append(case(Input=("attack", "defend"), Output=False))
        self.testcases.append(case(Input=("kelb", "kelb"), Output=True))
        self.testcases.append(case(Input=("abcd", "dcba"), Output=False))
        self.testcases.append(case(Input=("abcdb", "abcda"), Output=False))

    def get_testcases(self):
        return self.testcases
