import solution
from functools import lru_cache


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.largestMagicSquare([x[:] for x in test_input])

    def largestMagicSquare(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])

        @lru_cache(None)
        def dfs(posts, o):
            a, b, c, d = posts
            if a == c and b == d:
                return grid[a][b]
            if o == 0:
                return dfs((a, b, c, d - 1), o) + grid[c][d]
            elif o == 1:
                return dfs((a, b, c - 1, d), o) + grid[c][d]
            elif o == 2:
                return dfs((a, b, c - 1, d - 1), o) + grid[c][d]
            return dfs((a, b, c - 1, d + 1), o) + grid[c][d]

        def helper(k):
            for i in range(m - k + 1):
                for j in range(n - k + 1):
                    ans = dfs((i, j, i, j + k - 1), 0)
                    if dfs((i, j, i + k - 1, j + k - 1), 2) != ans:
                        continue
                    if dfs((i, j + k - 1, i + k - 1, j), 3) != ans:
                        continue
                    equal = True
                    for l in range(k):
                        if dfs((i + l, j, i + l, j + k - 1), 0) != ans:
                            equal = False
                            break
                        if dfs((i, j + l, i + k - 1, j + l), 1) != ans:
                            equal = False
                            break
                    if equal:
                        return True
            return False

        for i in range(min(m, n), 1, -1):
            if helper(i):
                return i
        return 1
