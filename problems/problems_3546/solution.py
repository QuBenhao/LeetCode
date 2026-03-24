import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.canPartitionGrid(test_input)

    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        # 计算总和
        total = sum(sum(row) for row in grid)
        # 检查水平分割
        row_sum = 0
        for i in range(m - 1):
            row_sum += sum(grid[i])
            if (d := row_sum * 2) == total:
                return True
            elif d > total:
                break
        # 检查垂直分割
        col_sum = 0
        for j in range(n - 1):
            col_sum += sum(grid[i][j] for i in range(m))
            if (d := col_sum * 2) == total:
                return True
            elif d > total:
                break
        return False
