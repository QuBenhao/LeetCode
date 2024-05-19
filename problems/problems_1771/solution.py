import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.longestPalindrome(*test_input)

    def longestPalindrome(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        # dp[i][j] = dp[i+1][j-1] + 2 if s[i] == s[j], else = max(dp[i+1][j], dp[i][j-1])
        s = word1 + word2
        dp = [[0] * len(s) for _ in range(len(s))]

        res = 0
        for i in range(len(s) - 1, -1, -1):
            dp[i][i] = 1
            for j in range(i + 1, len(s)):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                    if i < len(word1) <= j:
                        res = max(res, dp[i][j])
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

        return res
