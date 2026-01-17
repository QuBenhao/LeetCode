import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.largestSquareArea(*test_input)

    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        n = len(bottomLeft)
        ans = 0
        for i, ((x0, y0), (x1, y1)) in enumerate(zip(bottomLeft, topRight)):
            for j in range(i + 1, n):
                (x2, y2), (x3, y3) = bottomLeft[j], topRight[j]
                c, d, a, b = min(x1, x3), min(y1, y3), max(x0, x2), max(y0, y2)
                if a < c and b < d:
                    ans = max(ans, min(d - b, c - a) ** 2)
        return ans
