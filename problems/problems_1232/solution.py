import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.checkStraightLine(test_input)

    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        """
        (y1 - y0) / (x1 - x0) = (y2 - y0) / (x2 - x0)
        y1x2 - y0x2 - y1x0 = y2x1 - y0x1 - y2x0
        x0y2 - x0y1 + x1y0 -x1y2 + x2y1 - x2y0 = 0
        (x1y0 - x0y1) + x2 * (y1 - y0) + y2 * (x0 - x1) = 0
        """
        yd, xd, c = (coordinates[1][1] - coordinates[0][1],
                     coordinates[1][0] - coordinates[0][0],
                     coordinates[0][0] * coordinates[1][1] - coordinates[0][1] * coordinates[1][0])
        for x, y in coordinates[2:]:
            if x * yd - y * xd != c:
                return False
        return True
