from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input="(abcd)", Output="dcba"))
        self.testcases.append(case(Input="(u(love)i)", Output="iloveu"))
        self.testcases.append(case(Input="(ed(et(oc))el)", Output="leetcode"))
        self.testcases.append(case(Input="a(bcdefghijkl(mno)p)q", Output="apmnolkjihgfedcbq"))

    def get_testcases(self):
        return self.testcases
