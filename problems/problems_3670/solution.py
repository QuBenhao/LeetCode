import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maxProduct(test_input)

    def maxProduct(self, nums: List[int]) -> int:
        w = max(nums).bit_length()
        u = 1 << w
        dp = [0] * u
        for x in nums:
            dp[x] = x

        # SOS DP
        for i in range(w):
            j = 0
            while j < u:
                j |= 1 << i
                v = dp[j ^ (1 << i)]
                if v > dp[j]:
                    dp[j] = v
                j += 1
        return max(x * dp[(u - 1) ^ x] for x in nums)
