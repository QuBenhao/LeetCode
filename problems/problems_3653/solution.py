import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.xorAfterQueries(*test_input)

    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        for l, r, k, v in queries:
            for i in range(l, r + 1, k):
                nums[i] = (nums[i] * v) % MOD
        ans = 0
        for num in nums:
            ans ^= num
        return ans

MOD = 10**9 + 7
