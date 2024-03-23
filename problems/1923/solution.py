import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.longestCommonSubpath(*test_input)

    def longestCommonSubpath(self, n, paths):
        """
        :type n: int
        :type paths: List[List[int]]
        :rtype: int
        """
