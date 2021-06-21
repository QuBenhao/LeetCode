from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=1,Output=["0:01","0:02","0:04","0:08","0:16","0:32","1:00","2:00","4:00","8:00"]))
        self.testcases.append(case(Input=9,Output=[]))

    def get_testcases(self):
        return self.testcases
