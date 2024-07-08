import solution
from typing import *
from heapq import nlargest, nsmallest
from math import inf

class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minimumDistance(test_input)

    def minimumDistance(self, points: List[List[int]]) -> int:
        max_x1, max_x2 = nlargest(2, (x + y for x, y in points))  # x 最大次大
        min_x1, min_x2 = nsmallest(2, (x + y for x, y in points))  # x 最小次小
        max_y1, max_y2 = nlargest(2, (y - x for x, y in points))  # y 最大次大
        min_y1, min_y2 = nsmallest(2, (y - x for x, y in points))  # y 最小次小

        ans = inf
        for x, y in points:
            x, y = x + y, y - x
            dx = (max_x2 if x == max_x1 else max_x1) - (min_x2 if x == min_x1 else min_x1)
            dy = (max_y2 if y == max_y1 else max_y1) - (min_y2 if y == min_y1 else min_y1)
            ans = min(ans, max(dx, dy))
        return ans
