from math import inf

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.numberOfPairs(test_input)

    def numberOfPairs(self, points: List[List[int]]) -> int:
        points.sort(key=lambda p: (p[0], -p[1]))
        ans = 0
        for i, (_, y1) in enumerate(points):
            max_y = -inf
            for j in range(i + 1, len(points)):
                if y1 >= (y2 := points[j][1]) > max_y:
                    max_y = y2
                    ans += 1
                elif max_y == y1:
                    break
        return ans
