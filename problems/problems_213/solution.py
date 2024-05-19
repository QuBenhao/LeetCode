import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.rob(list(test_input))

    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # """
        # 常规动态规划解单排偷窃问题
        # """
        # def rob_(ns):
        #     n = len(ns)
        #     dp = [0] * n
        #     for i in range(n):
        #         # 当前的最大值是 上一次最大值 和 上上次最大值加上当前值 之间的最大值
        #         dp[i] = max(dp[i-1], dp[i-2] + ns[i])
        #     return dp[-1]
        #
        # if len(nums) == 1:
        #     return nums[0]
        # elif len(nums) == 2:
        #     return max(nums[0], nums[1])
        # else:
        #     return max(rob_(nums[:-1]),rob_(nums[1:]))

        """
        因为第一个和最后一个永远不能同时取，看作是0-n-2和1-n-1两种序列。一个从0开始，一个从1开始。
        rob 肯定是上一次没抢加上当前的nums[i]，而nrob则是上一次抢了和上一次没抢中的最大值。
        """
        n = len(nums)
        if n == 1:
            return nums[0]
        # start from 0, 1
        rob0 = nrob0 = rob1 = nrob1 = 0
        for i in range(n-1):
            rob0, nrob0 = nrob0 + nums[i], max(rob0, nrob0)
            rob1, nrob1 = nrob1 + nums[i+1], max(rob1, nrob1)
        return max(rob0, rob1, nrob0, nrob1)
