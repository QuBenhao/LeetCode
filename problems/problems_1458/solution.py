from functools import cache
from math import inf

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maxDotProduct(*test_input)

    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)
        @cache
        def dfs(i, j):
            if i == m or j == n:
                return -inf

            ans = max(dfs(i + 1, j + 1), 0) + nums1[i] * nums2[j]
            ans = max(ans, dfs(i + 1, j))
            ans = max(ans, dfs(i, j + 1))
            return ans

        return dfs(0, 0)
