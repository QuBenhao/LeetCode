import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minRectanglesToCoverPoints(*test_input)

    def minRectanglesToCoverPoints(self, points: List[List[int]], w: int) -> int:
        poi = sorted(set(p[0] for p in points))
        ans = idx = 0
        while idx < len(poi):
            ans += 1
            cur = poi[idx] + w
            while idx < len(poi) and poi[idx] <= cur:
                idx += 1
        return ans
