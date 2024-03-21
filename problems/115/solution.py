import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.numDistinct(*test_input)

    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """

        m, n = len(s), len(t)

        dp = [1] + [0] * n

        for i in range(1, m + 1):
            for j in range(min(i,n), 0, -1):
                if s[i - 1] == t[j - 1]:
                    dp[j] += dp[j - 1]

        return dp[-1]

        # m, n = len(s), len(t)
        #
        # dp = [[1] * (m + 1)] + [[0] * (m + 1) for _ in range(n)]
        #
        # for i in range(n):
        #     for j in range(m):
        #         dp[i + 1][j + 1] += dp[i + 1][j]
        #         if t[i] == s[j]:
        #             dp[i + 1][j + 1] += dp[i][j]
        #
        # return dp[-1][-1]
