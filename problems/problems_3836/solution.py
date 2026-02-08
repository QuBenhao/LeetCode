from functools import cache
from math import inf

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maxScore(*test_input)

    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        n, m = len(nums1), len(nums2)
        @cache
        def dfs(i, j, r):
            if n - i < r or m - j < r:
                return -inf
            if r == 0:
                return 0
            if i == n or j == m:
                return -inf
            return max(dfs(i + 1, j, r), dfs(i, j + 1, r), dfs(i + 1, j + 1, r - 1) + nums1[i] * nums2[j])

        return dfs(0, 0, k)
