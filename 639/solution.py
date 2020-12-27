import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.numDecodings(str(test_input))

    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
