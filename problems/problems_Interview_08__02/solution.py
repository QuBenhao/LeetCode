import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.pathWithObstacles(test_input)

    def pathWithObstacles(self, obstacleGrid: List[List[int]]) -> List[List[int]]:
        ans = []
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        visited = [[False for _ in range(n)] for _ in range(m)]

        def backtrack(i, j):
            if obstacleGrid[i][j]:
                return False
            if visited[i][j]:
                return False
            visited[i][j] = True
            ans.append([i, j])
            if i == m - 1 and j == n - 1:
                return True
            if j < n - 1 and backtrack(i, j + 1):
                return True
            if i < m - 1 and backtrack(i + 1, j):
                return True
            ans.pop()
            return False

        backtrack(0, 0)
        return ans
