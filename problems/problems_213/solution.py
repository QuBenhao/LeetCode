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
        # Standard dynamic programming for robbing a single row of houses
        # """
        # def rob_(ns):
        #     n = len(ns)
        #     dp = [0] * n
        #     for i in range(n):
        #         # The current maximum is the greater of the previous maximum and the maximum two steps ago plus the current value
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
        The first and last houses can never both be taken, so consider two sequences: 0 through n-2 and 1 through n-1. One starts at 0, the other at 1.
        rob is the previous value for not robbing plus the current nums[i]; nrob is the maximum of the previous robbing and not-robbing values.
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
