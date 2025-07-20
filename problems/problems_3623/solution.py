from collections import defaultdict

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.countTrapezoids(test_input)

    def countTrapezoids(self, points: List[List[int]]) -> int:
        group_by_y = defaultdict(int)
        for x, y in points:
            group_by_y[y] += 1
        ans = 0
        nums = [v * (v - 1) // 2 for v in group_by_y.values() if v > 1]
        total = sum(nums)
        for v in nums:
            total -= v
            ans = (ans + v * total) % (10**9 + 7)
        return ans
