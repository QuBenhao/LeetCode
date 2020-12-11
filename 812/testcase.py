from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=[[0, 0], [0, 1], [1, 0], [0, 2], [2, 0]], Output=2))
        self.testcases.append(case(Input=[[-35,19],[40,19],[27,-20],[35,-3],[44,20],[22,-21],[35,33],[-19,42],[11,47],[11,37]],Output=1799))

    def get_testcases(self):
        return self.testcases
