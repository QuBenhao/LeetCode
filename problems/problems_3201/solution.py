import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maximumLength(test_input)

    def maximumLength(self, nums: List[int]) -> int:
        dp = [0] * 4
        for num in nums:
            cur = num % 2
            for i in range(4):
                if (i >> (dp[i] % 2)) & 1 == cur:
                    dp[i] += 1
        return max(dp)
