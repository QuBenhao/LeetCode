from math import inf

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maxDistinctElements(*test_input)

    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans = 0
        cur = -inf
        for num in nums:
            if num + k == cur:
                continue
            ans += 1
            if num - k > cur:
                cur = num - k
            else:
                cur += 1
        return ans
