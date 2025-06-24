import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.sumSubseqWidths(test_input)

    def sumSubseqWidths(self, nums: List[int]) -> int:
        ans = 0
        nums.sort()
        n = len(nums)
        powers = [1] * n
        for i in range(1, n):
            powers[i] = powers[i - 1] * 2 % MOD
        for i, num in enumerate(nums):
            ans = (ans + num * (powers[i] - powers[n - 1 - i])) % MOD
        return ans

MOD = 10**9 + 7
