import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maxSubArray(test_input)

    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # # dynamic programming
        n = len(nums)

        dp = [nums[i] for i in range(n)]

        for i in range(1,n):
            dp[i] = max(dp[i-1]+nums[i],nums[i])

        return max(dp)

        # # divide and conquer
        # def div_con_sum(left, right):
        #     if left == right:
        #         return nums[left]
        #
        #     center = (left + right) // 2
        #     l_sum = div_con_sum(left, center)
        #     r_sum = div_con_sum(center + 1, right)
        #
        #     ls = rs = 0
        #     l_max = r_max = float("-inf")
        #     for i in range(center, left - 1, -1):
        #         ls += nums[i]
        #         if ls > l_max:
        #             l_max = ls
        #     for i in range(center + 1, right + 1):
        #         rs += nums[i]
        #         if rs > r_max:
        #             r_max = rs
        #     m = max(l_sum, r_sum, l_max + r_max)
        #     return m
        #
        # return div_con_sum(0, len(nums) - 1)
