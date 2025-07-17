import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maximumLength(*test_input)

    def maximumLength(self, nums: List[int], k: int) -> int:
        # dp = [[0] * k for _ in range(k)]
        # for x in nums:
        #     cur = x % k
        #     for y, length in enumerate(dp[cur]):
        #         dp[y][cur] = length + 1
        # return max(map(max, dp))

        ans = 0
        for val in range(k):
            dp = [0] * k
            for num in nums:
                num %= k
                dp[num] = dp[val - num] + 1
            ans = max(ans, max(dp))
        return ans
