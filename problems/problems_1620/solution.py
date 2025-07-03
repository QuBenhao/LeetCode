from math import floor

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.bestCoordinate(*test_input)

    def bestCoordinate(self, towers: List[List[int]], radius: int) -> List[int]:
        ans = 0
        ans_x, ans_y = 0, 0
        radius = radius ** 2
        for x in range(51):
            for y in range(51):
                total_quality = 0
                for qx, qy, quality in towers:
                    if (d := (qx - x) ** 2 + (qy - y) ** 2) <= radius:
                        total_quality += floor(quality / (1 + d ** 0.5))
                if total_quality > ans:
                    ans = total_quality
                    ans_x, ans_y = x, y
        return [ans_x, ans_y]
