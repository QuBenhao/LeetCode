import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minCut(test_input)

    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """

        def central_extend(string, left, right, dp):
            while left >= 0 and right < len(string) and string[left] == string[right]:
                dp[right] = min(dp[right], dp[left - 1] + 1 if left > 0 else 0)
                left -= 1
                right += 1

        # check special cases first to save time
        if s == s[::-1]:
            return 0

        n = len(s)

        for i in range(1, n):
            if s[:i] == s[:i][::-1] and s[i + 1:] == s[i + 1:][::-1]:
                return 1

        dp = [i for i in range(n)]
        for i in range(n):
            # 寻找以i为中心的最长奇数回文串
            central_extend(s, i, i, dp)
            # 寻找以i,i+1为中心的最长偶数回文串
            central_extend(s, i, i + 1, dp)
        return dp[-1]

        # n = len(s)
        #
        # is_palindrome = [[True for _ in range(n)] for _ in range(n)]
        # for i in range(n):
        #     for j in range(i):
        #         is_palindrome[j][i] = s[j] == s[i] and is_palindrome[j + 1][i - 1]
        #
        # dp = [i for i in range(n)]
        # for i in range(n):
        #     if is_palindrome[0][i]:
        #         dp[i] = 0
        #     else:
        #         for j in range(1, i + 1):
        #             if is_palindrome[j][i]:
        #                 dp[i] = min(dp[i], dp[j - 1] + 1)
        #
        # return dp[-1]
