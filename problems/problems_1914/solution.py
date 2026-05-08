import solution
from typing import List


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.rotateGrid(*test_input)

    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])

        for layer in range(min(m, n) // 2):
            top, left = layer, layer
            bottom, right = m - 1 - layer, n - 1 - layer

            # 生成该层坐标（逆时针顺序）
            coords = []
            for j in range(left, right):
                coords.append((top, j))
            for i in range(top, bottom):
                coords.append((i, right))
            for j in range(right, left, -1):
                coords.append((bottom, j))
            for i in range(bottom, top, -1):
                coords.append((i, left))

            # 提取、旋转、写回
            vals = [grid[i][j] for i, j in coords]
            shift = k % len(vals)
            vals = vals[shift:] + vals[:shift]

            for (i, j), v in zip(coords, vals):
                grid[i][j] = v

        return grid
