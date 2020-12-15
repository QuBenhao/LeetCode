import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minCut(test_input)

    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """

        def is_palindrome(string):
            if string in palindrome:
                return True
            if string == string[::-1]:
                palindrome.add(string)
                return True
            return False

        if s == s[::-1]:
            return 0

        n = len(s)
        palindrome = set()
        dp = [i for i in range(n)]

        for i in range(n):
            for j in range(i+1, n):
                if is_palindrome(s[i:j]):
                    if i == 0:
                        if j > 0:
                            dp[j - 1] = 0
                        dp[j] = min(dp[j], 1)
                    else:
                        if j > 0:
                            dp[j-1] = min(dp[j-1], dp[i - 1] + 1)
                        dp[j] = min(dp[j], dp[i - 1] + 2)
            if is_palindrome(s[i:]):
                dp[-1] = min(dp[-1], dp[i - 1] + 1)

        return dp[-1]
