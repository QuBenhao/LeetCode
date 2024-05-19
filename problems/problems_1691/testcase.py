from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=[[50, 45, 20], [95, 37, 53], [45, 23, 12]], Output=190))
        self.testcases.append(case(Input=[[38, 25, 45], [76, 35, 3]], Output=76))
        self.testcases.append(
            case(Input=[[7, 11, 17], [7, 17, 11], [11, 7, 17], [11, 17, 7], [17, 7, 11], [17, 11, 7]], Output=102))
        self.testcases.append(
            case(
                Input=[[53, 38, 26], [32, 46, 20], [9, 20, 48], [76, 30, 73], [81, 50, 60], [15, 31, 94], [100, 65, 50],
                       [97, 78, 57], [90, 41, 86], [50, 95, 44], [60, 39, 18], [56, 39, 98], [53, 63, 58], [61, 97, 93],
                       [80, 26, 30], [90, 81, 93], [93, 7, 25], [95, 75, 78]], Output=476)
        )

    def get_testcases(self):
        return self.testcases
