import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.checkOnesSegment(str(test_input))

    def checkOnesSegment(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return '0' not in s[s.index('1'):len(s) - s[::-1].index('1')]
