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
        if m == n:
            return 1
        if n > m:
            m,n = n,m
        return 1 + self.tilingRectangle(m-n,n)
