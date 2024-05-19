import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maxAreaOfIsland([x[:] for x in test_input])

    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])

        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n or not grid[i][j]:
                return 0
            cur = 1
            grid[i][j] = 0
            for di, dj in (-1,0),(1,0),(0, 1),(0, -1):
                cur += dfs(i+di, j+dj)
            return cur

        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    ans = max(ans, dfs(i, j))
        return ans
