import solution
from math import inf


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maxPoints([x[:] for x in test_input])

    def maxPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        m = len(points)
        n = len(points[0])
        dp = points[0]
        for i in range(1, m):
            new_dp = list(dp)
            left_max = -inf
            right_max = -inf
            for j in range(n):
                left_max = max(left_max, dp[j] + j)
                right_max = max(right_max, dp[n-1-j] - n + 1 + j)
                new_dp[j] = max(left_max - j + points[i][j], new_dp[j])
                new_dp[n-1-j] = max(n - 1 - j + right_max + points[i][n-1-j], new_dp[n-1-j])
            dp = new_dp
        return max(dp)
