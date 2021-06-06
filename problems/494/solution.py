import solution
from functools import lru_cache
from collections import Counter


class Solution(solution.Solution):
    def solve(self, test_input=None):
        nums, target = test_input
        return self.findTargetSumWays(list(nums), target)

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
        #     # 后面全取正也到不了 或者说 后面全取负也到不了
        #     if abs(target - t) > presum[-1] - presum[idx]:
        #         return 0
        #     return dfs(idx + 1, t + nums[idx]) + dfs(idx + 1, t - nums[idx])
        # n = len(nums)
        # presum = [0] * (n + 1)
        # for i in range(n):
        #     presum[i + 1] = presum[i] + nums[i]
        # return dfs(0, 0)

        # target为取正的数的和减去取负的数的和
        # 假设正数和为a, 那么负数的和为 s - a且 a-(s-a) = target
        # 可得 a= (target+s)//2
        # 所以实际上要找的就是和为(target+s)//2的组合数
        t = target + sum(nums)
        if t % 2 != 0 or t < 0 or t - target * 2 < 0:
            return 0
        t //= 2
        dp = [0] * (t+1)
        dp[0] = 1
        for num in nums:
            # 从后往前更新,之前取到i-num个的时候，取i的方案数又多了取之前的i-num的方案数加上取num
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


