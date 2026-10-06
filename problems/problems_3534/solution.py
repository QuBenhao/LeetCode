from collections import deque

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.pathExistenceQueries(*test_input)

    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[int]:
        idx = sorted(range(n), key=lambda i: nums[i]) # Map sorted indices of nums to original indices
        mapping = {j: i for i, j in enumerate(idx)} # Map original indices of nums to sorted indices

        m = n.bit_length()
        pa = [[0] * m for _ in range(n)] # pa[i][j] is the farthest node (sorted index) reachable from i (sorted index) in 2^j steps

        left = 0
        for i, j in enumerate(idx):
            while nums[j] - nums[idx[left]] > maxDiff: # Find the leftmost reachable node
                left += 1
            pa[i][0] = left

        for j in range(1, m):
            for i in range(n):
                pa[i][j] = pa[pa[i][j - 1]][j - 1] # Binary lifting

        ans = [-1] * len(queries)
        for i, (l, r) in enumerate(queries):
            if l == r:
                ans[i] = 0
                continue
            l, r = mapping[l], mapping[r]
            if l > r:
                l, r = r, l
            res = 0
            for k in range(m - 1, -1, -1):
                if pa[r][k] > l:
                    r = pa[r][k]
                    res |= 1 << k
            ans[i] = -1 if pa[r][0] > l else res + 1
        return ans
