from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=("abaca", [[0, 1], [0, 2], [2, 3], [3, 4]]), Output=3))
        self.testcases.append(case(Input=("a", [[0, 0]]), Output=-1))
        self.testcases.append(case(Input=["hhqhuqhqff",[[0,1],[0,2],[2,3],[3,4],[3,5],[5,6],[2,7],[6,7],[7,8],[3,8],[5,8],[8,9],[3,9],[6,9]]], Output=3))

    def get_testcases(self):
        return self.testcases
