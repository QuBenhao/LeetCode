import solution
from collections import defaultdict


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.largestDivisibleSubset(list(test_input))

    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        dp = defaultdict(list)
        ans = []
        for num in nums:
            max_list = []
            for key, val in dp.items():
                if num % key == 0 and len(val) > len(max_list):
                    max_list = val
            if not max_list:
                dp[num] = [num]
            else:
                dp[num] = max_list + [num]
            if len(dp[num]) > len(ans):
                ans = dp[num]
        return ans

        # nums.sort()
        # n = len(nums)
        # dp = [[num] for num in nums]
        # for i in range(n):
        #     for j in range(i):
        #         if nums[i] % nums[j] == 0 and len(dp[j]) + 1 > len(dp[i]):
        #             dp[i] = dp[j] + [nums[i]]
        # return max(dp,key=len)
