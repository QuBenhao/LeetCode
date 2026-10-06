import solution
from functools import lru_cache
from collections import Counter


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.findTargetSumWays(*test_input)

    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # @lru_cache(None)
        # def dfs(idx, t):
        #     if idx == n:
        #         if t == target:
        #             return 1
        #         return 0
        #     # The target is unreachable even if all remaining values are positive or all are negative
        #     if abs(target - t) > presum[-1] - presum[idx]:
        #         return 0
        #     return dfs(idx + 1, t + nums[idx]) + dfs(idx + 1, t - nums[idx])
        # n = len(nums)
        # presum = [0] * (n + 1)
        # for i in range(n):
        #     presum[i + 1] = presum[i] + nums[i]
        # return dfs(0, 0)

        # target is the sum of values assigned + minus the sum of values assigned -
        # If the positive-side sum is a, the negative-side sum is s - a, and a-(s-a) = target
        # Thus, a = (target+s)//2
        # Count combinations whose sum is (target+s)//2
        t = target + sum(nums)
        if t % 2 != 0 or t < 0 or t - target * 2 < 0:
            return 0
        t //= 2
        dp = [0] * (t+1)
        dp[0] = 1
        for num in nums:
            # Update backward: each previous way to reach i-num yields another way to reach i by taking num
            for i in range(t,num-1,-1):
                dp[i] += dp[i-num]
        return dp[t]

        # dp = Counter()
        # dp[0] = 2 ** nums.count(0)
        # for num in nums:
        #     if not num:
        #         continue
        #     for key in sorted(dp.keys(), reverse=True):
        #         if key <= t - num:
        #             dp[num + key] += dp[key]
        # return dp[t]
