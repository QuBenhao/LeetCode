from itertools import pairwise
from math import inf

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minimumPairRemoval(test_input)

    def minimumPairRemoval(self, nums: List[int]) -> int:
        ans = 0
        while nums != sorted(nums):
            cur, cur_v = -1, inf
            for i, (a, b) in enumerate(pairwise(nums)):
                if cur_v > a + b:
                    cur, cur_v = i, a + b
            nums.pop(cur)
            nums[cur] = cur_v
            ans += 1
        return ans
