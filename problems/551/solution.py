import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.checkRecord(str(test_input))

    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return "LLL" not in s and s.count('A') < 2
