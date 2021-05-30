from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=("acb", "cba", "cdb"), Output=True))
        self.testcases.append(case(Input=("aaa", "a", "aab"), Output=False))
        self.testcases.append(case(Input=("aaa", "a", "aaaa"), Output=True))

    def get_testcases(self):
        return self.testcases
