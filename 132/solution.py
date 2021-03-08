import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minCut(test_input)

    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """

        n = len(s)

        is_palindrome = [[True for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(i):
                is_palindrome[j][i] = s[j] == s[i] and is_palindrome[j + 1][i - 1]

        dp = [i for i in range(n)]
        for i in range(n):
            if is_palindrome[0][i]:
                dp[i] = 0
            else:
                for j in range(1, i + 1):
                    if is_palindrome[j][i]:
                        dp[i] = min(dp[i], dp[j - 1] + 1)

        return dp[-1]
