from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=(
        ["SeatManager", "reserve", "reserve", "unreserve", "reserve", "reserve", "reserve", "reserve", "unreserve"],
        [[5], [], [], [2], [], [], [], [], [5]]), Output=[None, 1, 2, None, 2, 3, 4, 5, None]))
        self.testcases.append(case(Input=[["SeatManager","reserve","reserve","unreserve","reserve","reserve","reserve","reserve","unreserve"],[[5],[],[],[2],[],[],[],[],[5]]], Output=[None,1,2,None,2,3,4,5,None]))

    def get_testcases(self):
        return self.testcases
