from math import inf
from typing import *

import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minArraySum(*test_input)

    def minArraySum(self, nums: List[int], k: int) -> int:
        g = [inf] * (k + 1)
        g[0] = 0
        mod = 0
        cur = 0
        for num in nums:
            mod = (mod + num) % k
            cur = min(cur + num, g[mod])
            g[mod] = min(g[mod], cur)
        return cur
