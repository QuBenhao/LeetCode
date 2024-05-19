from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=["un","iq","ue"], Output=4))
        self.testcases.append(case(Input=["cha","r","act","ers"], Output=6))
        self.testcases.append(case(Input=["abcdefghijklmnopqrstuvwxyz"], Output=26))


    def get_testcases(self):
        return self.testcases