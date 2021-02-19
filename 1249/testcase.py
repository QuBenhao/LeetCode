from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input="lee(t(c)o)de)", Output=["lee(t(c)o)de", "lee(t(co)de)", "lee(t(c)ode)"]))
        self.testcases.append(case(Input="a)b(c)d", Output="ab(c)d"))
        self.testcases.append(case(Input="))((", Output=""))
        self.testcases.append(case(Input="(a(b(c)d)", Output="a(b(c)d)"))
        self.testcases.append(case(Input="())()(((", Output="()()"))

    def get_testcases(self):
        return self.testcases
