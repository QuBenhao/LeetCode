import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maximumScore(*test_input)

    def maximumScore(self, nums, multipliers):
        """
        :type nums: List[int]
        :type multipliers: List[int]
        :rtype: int
        """
        n, m = len(nums), len(multipliers)
        dp = [[0 for _ in range(m+1)] for _ in range(m+1)]
        res = float("-inf")
        for i in range(m+1):
            for j in range(m+1-i):
                if j > 0 and i > 0:
                    dp[i][j] = max(dp[i-1][j] + multipliers[i+j-1] * nums[i-1],
                                   dp[i][j-1] + multipliers[i+j-1] * nums[n-j])
                elif j > 0:
                    dp[i][j] = dp[i][j-1] + multipliers[j-1] * nums[n-j]
                elif i > 0:
                    dp[i][j] = dp[i-1][j] + multipliers[i-1] * nums[i-1]
                if i + j == m:
                    res = max(res, dp[i][j])
        return res
