from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=("great", "rgeat"), Output=True))
        self.testcases.append(case(Input=("abcde", "caebd"), Output=False))
        self.testcases.append(case(Input=("a", "a"), Output=True))


    def get_testcases(self):
        return self.testcases
