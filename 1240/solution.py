import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        n,m = test_input
        return self.tilingRectangle(n,m)

    def tilingRectangle(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """

