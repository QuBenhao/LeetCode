import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.sumOfPowers(*test_input)

    def sumOfPowers(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        mod = 10 ** 9 + 7

        def f(nums, lower_diff):
            n = len(nums)
            dp = [[0] * k for _ in range(n)]
            dp_acc = [[0] * k for _ in range(n + 1)]
            pt = 0
            dp[0][1] = 1
            dp_acc[1][1] = 1
            for i in range(1, n):
                while pt < i and nums[i] - nums[pt] >= lower_diff:
                    pt += 1

                for v in range(k - 1):
                    dp[i][v + 1] += dp_acc[pt][v]
                    dp[i][v + 1] %= mod

                for v in range(k):
                    dp_acc[i + 1][v] = dp_acc[i][v] + dp[i][v]
                    dp_acc[i + 1][v] %= mod

            return dp_acc[-1]

        ans = 0
        for i in range(n):
            for j in range(i):
                v = nums[i] - nums[j]
                vs = [nums[j] - nums[idx] for idx in range(j, -1, -1)]
                dp1 = f(vs, v + 1)
                vs = [nums[idx] - nums[i] for idx in range(i, n)]
                dp2 = f(vs, v)
                for x in range(1, k):
                    ans += dp1[x] * dp2[k - x] * v
                    ans %= mod
        return ans
