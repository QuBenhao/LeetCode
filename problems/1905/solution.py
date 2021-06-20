import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        grid1, grid2 = test_input
        return self.countSubIslands([x[:] for x in grid1], [x[:] for x in grid2])

    def countSubIslands(self, grid1, grid2):
        """
        :type grid1: List[List[int]]
        :type grid2: List[List[int]]
        :rtype: int
        """
        def dfs(i, j):
            if i < 0 or j < 0 or i == m or j == n or not grid2[i][j] or (i, j) in explored:
                return -1
            if not grid1[i][j]:
                return 0
            explored.add((i, j))

            mark = 1
            for dx, dy in (0, 1), (0, -1), (1, 0), (-1, 0):
                if not dfs(i + dx, j + dy):
                    mark = 0
            return mark

        m, n = len(grid1), len(grid1[0])
        explored = set()
        ans = 0

        for i in range(m):
            for j in range(n):
                if grid2[i][j] and (i, j) not in explored:
                    if dfs(i, j) == 1:
                        ans += 1
        return ans
