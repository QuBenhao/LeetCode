import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.longestNiceSubstring(str(test_input))

    def longestNiceSubstring(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        if n < 2:
            return ""
        chars = set(s)
        for i in range(n):
            if s[i].swapcase() not in chars:
                s1 = self.longestNiceSubstring(s[:i])
                s2 = self.longestNiceSubstring(s[i+1:])
                return max(s1, s2, key=len)
        return s
