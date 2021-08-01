import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.countSpecialSubsequences(list(test_input))

    def countSpecialSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [0, 0, 0, 1]
        for num in nums:
            dp[num] += dp[num - 1] + dp[num]
        return dp[2] % (10 ** 9 + 7)
