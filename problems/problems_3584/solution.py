from collections import deque

from math import inf

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maximumProduct(*test_input)

    def maximumProduct(self, nums: List[int], m: int) -> int:
        if m == 1:
            return max(a * a for a in nums)
        pre_max = [-inf] * len(nums)
        pre_min = [inf] * len(nums)
        ans = -inf
        for i, num in enumerate(nums):
            if i >= m - 1:
                ans = max(ans, num * pre_max[i + 1 - m], num * pre_min[i + 1 - m])
            pre_max[i] = max(pre_max[i], num)
            pre_min[i] = min(pre_min[i], num)
            if i > 0:
                pre_max[i] = max(pre_max[i], pre_max[i - 1])
                pre_min[i] = min(pre_min[i], pre_min[i - 1])
        return ans
