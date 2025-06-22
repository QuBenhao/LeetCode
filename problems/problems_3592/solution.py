import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.findCoins(test_input)

    def findCoins(self, numWays: List[int]) -> List[int]:
        n = len(numWays)
        dp = [0] * (n + 1)
        dp[0] = 1
        ans = []
        for i in range(1, n + 1):
            cur = numWays[i - 1]
            if dp[i] == cur - 1:
                ans.append(i)
                dp[i] += 1
                for j in range(i + 1, n + 1):
                    dp[j] += dp[j-i]
            elif dp[i] != cur:
                return []
        return ans
