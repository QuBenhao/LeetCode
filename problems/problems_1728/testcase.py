from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=(["####F", "#C...", "M...."], 1, 2), Output=True))
        self.testcases.append(case(Input=(["M.C...F"], 1, 4), Output=True))
        self.testcases.append(case(Input=(["M.C...F"], 1, 3), Output=False))
        self.testcases.append(case(Input=(["C...#", "...#F", "....#", "M...."], 2, 5), Output=False))
        self.testcases.append(case(Input=([".M...", "..#..", "#..#.", "C#.#.", "...#F"], 3, 1), Output=True))
        self.testcases.append(case(Input=[["C#......","M..####.","###.....","....####",".####...","......#.","#######.","F......."],1,1], Output=True))

    def get_testcases(self):
        return self.testcases
