from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input="tree", Output="eert"))
        self.testcases.append(case(Input="cccaaa", Output="aaaccc"))
        self.testcases.append(case(Input="Aabb", Output="bbAa"))

    def get_testcases(self):
        return self.testcases
