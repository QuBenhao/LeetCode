from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=(
        [[".", ".", ".", "B", ".", ".", ".", "."], [".", ".", ".", "W", ".", ".", ".", "."],
         [".", ".", ".", "W", ".", ".", ".", "."], [".", ".", ".", "W", ".", ".", ".", "."],
         ["W", "B", "B", ".", "W", "W", "W", "B"], [".", ".", ".", "B", ".", ".", ".", "."],
         [".", ".", ".", "B", ".", ".", ".", "."], [".", ".", ".", "W", ".", ".", ".", "."]], 4, 3, "B"), Output=True))
        self.testcases.append(case(Input=(
        [[".", ".", ".", ".", ".", ".", ".", "."], [".", "B", ".", ".", "W", ".", ".", "."],
         [".", ".", "W", ".", ".", ".", ".", "."], [".", ".", ".", "W", "B", ".", ".", "."],
         [".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", ".", "B", "W", ".", "."],
         [".", ".", ".", ".", ".", ".", "W", "."], [".", ".", ".", ".", ".", ".", ".", "B"]], 4, 4, "W"), Output=False))

    def get_testcases(self):
        return self.testcases
