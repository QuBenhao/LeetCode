from collections import defaultdict
from math import inf

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.countTrapezoids(test_input)

    def countTrapezoids(self, points: List[List[int]]) -> int:
        cnt = defaultdict(lambda: defaultdict(int))  # Slope -> intercept -> count
        cnt2 = defaultdict(lambda: defaultdict(int))  # Midpoint -> slope -> count

        for i, (x, y) in enumerate(points):
            for x2, y2 in points[:i]:
                dy = y - y2
                dx = x - x2
                if dx == 0:
                    k = inf
                    b = float(x)
                else:
                    k = dy / dx
                    b = (y * dx - dy * x) / dx
                cnt[k][b] += 1  # Group by slope and intercept
                cnt2[(x + x2, y + y2)][k] += 1  # Group by midpoint and slope

        ans = 0
        for ct in cnt.values():
            s = 0
            for c in ct.values():
                ans += s * c
                s += c

        for ct in cnt2.values():
            s = 0
            for c in ct.values():
                ans -= s * c
                s += c

        return ans
