import solution
from functools import lru_cache


class Solution(solution.Solution):
    def solve(self, test_input=None):
        m, n, maxMove, startRow, startColumn = test_input
        return self.findPaths(m, n, maxMove, startRow, startColumn)

    def findPaths(self, m, n, maxMove, startRow, startColumn):
        """
        :type m: int
        :type n: int
        :type maxMove: int
        :type startRow: int
        :type startColumn: int
        :rtype: int
        """
        mod = 10 ** 9 + 7
        dirc = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        @lru_cache(None)
        def dfs(x, y, move):
            if x < 0 or x == m or y < 0 or y == n:
                return 1
            if not move or (m - move > x > move - 1 and n - move > y > move - 1):
                return 0
            ans = 0
            move -= 1
            for dx, dy in dirc:
                ans = (ans + dfs(x + dx, y + dy, move)) % mod
            return ans

        return dfs(startRow, startColumn, maxMove)
