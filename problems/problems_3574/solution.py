from math import gcd

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maxGCDScore(*test_input)

    def maxGCDScore(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [dict() for _ in range(n)]
        ans = 0
        for i in range(n):
            dp[i][nums[i]] = (1, 0) # (length, used)
            ans = max(ans, nums[i])
            if k > 0:
                dp[i][nums[i] * 2] = (1, 1)
                ans = max(ans, nums[i] * 2)
            if i > 0:
                for g, (l, u) in dp[i-1].items():
                    ng = gcd(g, nums[i])
                    if ng not in dp[i] or dp[i][ng][0] < l + 1 or (dp[i][ng][0] == l + 1 and dp[i][ng][1] > u):
                        dp[i][ng] = (l + 1, u)
                        ans = max(ans, (l+1)*ng)
                    if u < k:
                        ng2 = gcd(g, nums[i] * 2)
                        if ng2 not in dp[i] or dp[i][ng2][0] < l + 1 or (dp[i][ng2][0] == l + 1 and dp[i][ng2][1] > u + 1):
                            dp[i][ng2] = (l + 1, u + 1)
                            ans = max(ans, (l + 1) * ng2)
        return ans
