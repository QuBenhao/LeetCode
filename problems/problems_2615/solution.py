from collections import defaultdict

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.distance(test_input)

    def distance(self, nums: List[int]) -> List[int]:
        idx_map = defaultdict(list)
        for i, num in enumerate(nums):
            idx_map[num].append(i)
        ans = [0] * len(nums)
        for v in idx_map.values():
            s, n = sum(v), len(v)
            prefix = 0
            for k, i in enumerate(v):
                ans[i] = s - 2 * prefix + i * (2 * k - n)
                prefix += i
        return ans
