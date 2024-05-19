import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.findMinArrowShots(test_input)

    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x:x[1])
        cur, ans = points[0][1], 1
        for a, b in points:
            if a > cur:
                ans += 1
                cur = b
        return ans
