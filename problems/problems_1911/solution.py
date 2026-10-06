import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maxAlternatingSum(list(test_input))

    def maxAlternatingSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        # dp[i][0]: include i, end with -; dp[i][1]: include i, end with +; dp[i][2]: exclude i, end with -; dp[i][3]: exclude i, end with +
        dp0 = dp2 = dp3 = 0
        dp1 = nums[0]
        for i in range(1, n):
            dp0, dp1, dp2, dp3 = max(dp1 - nums[i], dp3 - nums[i]),\
                                 max(dp0 + nums[i], dp2 + nums[i]),\
                                 max(dp0, dp2),\
                                 max(dp1, dp3)
        return max(dp1, dp3)
