import solution
from itertools import accumulate


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.stoneGameVII(test_input)

    def stoneGameVII(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        n = len(stones)
        dp = [[0] * n for _ in range(n)]
        presum = [0] + list(accumulate(stones))
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                dp[i][j] = max(presum[j + 1] - presum[i + 1] - dp[i + 1][j], presum[j] - presum[i] - dp[i][j - 1])
        return dp[0][n - 1]
