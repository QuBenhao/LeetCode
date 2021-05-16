from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=("abpcplea", ["ale","apple","monkey","plea"]), Output="apple"))
        self.testcases.append(case(Input=("abpcplea",  ["a","b","c"]), Output="a"))

    def get_testcases(self):
        return self.testcases
