import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.isRobotBounded(test_input)

    def isRobotBounded(self, instructions: str) -> bool:
        dirs = [(0, 1), (-1, 0), (0, -1), (1, 0)]
        x, y, d = 0, 0, 0
        for ist in instructions:
            match ist:
                case "L":
                    d = (d + 1) % 4
                case "R":
                    d = (d - 1 + 4) % 4
                case _:
                    x, y = x + dirs[d][0], y + dirs[d][1]
        return (x == 0 and y == 0) or d != 0
