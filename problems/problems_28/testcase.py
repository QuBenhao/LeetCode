from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=("hello", "ll"), Output=2))
        self.testcases.append(case(Input=("aaaaa", "bba"), Output=-1))
        self.testcases.append(case(Input=("", ""), Output=0))
        self.testcases.append(case(Input=("aabaaabaaac", "aabaaac"), Output=4))
        self.testcases.append(case(Input=("mississippi", "issipi"), Output=-1))

    def get_testcases(self):
        return self.testcases
