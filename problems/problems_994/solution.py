import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.orangesRotting(test_input)

    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        fresh = 0
        q = []
        for i, row in enumerate(grid):
            for j, x in enumerate(row):
                if x == 1:
                    fresh += 1  # Count fresh oranges
                elif x == 2:
                    q.append((i, j))  # Oranges that are rotten initially

        ans = -1
        while q:
            ans += 1  # One minute passes
            tmp = q
            q = []
            for x, y in tmp:  # Oranges already rotten
                for i, j in (x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1):  # Four directions
                    if 0 <= i < m and 0 <= j < n and grid[i][j] == 1:  # Fresh orange
                        fresh -= 1
                        grid[i][j] = 2  # Turn into a rotten orange
                        q.append((i, j))

        return -1 if fresh else max(ans, 0)
