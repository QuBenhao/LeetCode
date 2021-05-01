import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.replaceDigits(str(test_input))

    def replaceDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans = ""
        for i,c in enumerate(s):
            if i % 2 == 0:
                ans += c
            else:
                ans += chr(ord(s[i-1]) + int(c))
        return ans
