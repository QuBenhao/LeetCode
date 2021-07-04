import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        n, paths = test_input
        return self.longestCommonSubpath(n, [x[:] for x in paths])

    def longestCommonSubpath(self, n, paths):
        """
        :type n: int
        :type paths: List[List[int]]
        :rtype: int
        """
