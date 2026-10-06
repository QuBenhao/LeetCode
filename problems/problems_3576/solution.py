import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.canMakeEqual(*test_input)

    def canMakeEqual(self, nums: List[int], k: int) -> bool:
        dp = [[0, False] for _ in range(2)] # dp[0] represents making all elements 1; dp[1] represents making all elements -1
        for num in nums:
            if num == 1:
                if dp[0][1]: # The previous flip made it 1; another flip is required now
                    dp[0][0] += 1
                if dp[1][1]:
                    # The previous flip made it -1; no flip is needed now
                    dp[1][1] = False
                else:
                    dp[1][0] += 1
                    dp[1][1] = True
            else:
                if dp[1][1]:
                    dp[1][0] += 1
                if dp[0][1]:
                    dp[0][1] = False
                else:
                    dp[0][0] += 1
                    dp[0][1] = True
            if dp[0][0] > k and dp[1][0] > k:
                return False
        return (not dp[0][1] and dp[0][0] <= k) or (not dp[1][1] and dp[1][0] <= k)
