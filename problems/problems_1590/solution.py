from math import inf

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minSubarray(*test_input)

    def minSubarray(self, nums: List[int], p: int) -> int:
        target = sum(nums) % p
        if not target:
            return 0
        pos = dict()
        pos[0] = -1
        s = 0
        ans = inf
        for i, num in enumerate(nums):
            s = (s + num) % p
            pos[s] = i
            if (res := (s - target) % p) in pos:
                ans = min(ans, i - pos[res])
        return -1 if ans == len(nums) else ans
