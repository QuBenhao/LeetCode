from functools import cache

from math import inf

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minXor(*test_input)

    def minXor(self, nums: List[int], k: int) -> int:
        n = len(nums)
        pre_xor = [0] * (n + 1)
        for _i in range(n):
            pre_xor[_i + 1] = pre_xor[_i] ^ nums[_i]

        @cache
        def dfs(i, k):
            if k == 1:
                return pre_xor[n] ^ pre_xor[i]
            ans = inf
            for j in range(i+1, n - k + 2):
                ans = min(ans, max(pre_xor[i] ^ pre_xor[j], dfs(j, k - 1)))
            return ans

        return dfs(0, k)
