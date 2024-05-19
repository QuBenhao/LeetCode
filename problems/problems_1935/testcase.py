from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=("hello world", "ad"), Output=1))
        self.testcases.append(case(Input=("leet code", "lt"), Output=1))
        self.testcases.append(case(Input=("leet code", "e"), Output=0))

    def get_testcases(self):
        return self.testcases
