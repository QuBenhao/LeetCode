import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.countSpecialSubsequences(list(test_input))

    def countSpecialSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp, mod = [0, 0, 0, 1], 10 ** 9 + 7
        for num in nums:
            dp[num] = (2 * dp[num] + dp[num - 1]) % mod
        return dp[2]
