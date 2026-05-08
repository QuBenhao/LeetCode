import solution
from typing import List


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.rotateGrid(*test_input)

    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        # 方向：右、下、左、上（逆时针）
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        for layer in range(min(m, n) // 2):
            top, left = layer, layer
            bottom, right = m - 1 - layer, n - 1 - layer
            # 各边长度
            lengths = [right - left, bottom - top, right - left, bottom - top]

            # 生成该层坐标（逆时针顺序）
            coords = []
            i, j = top, left
            for (di, dj), length in zip(dirs, lengths):
                for _ in range(length):
                    coords.append((i, j))
                    i += di
                    j += dj

            # 提取、旋转、写回
            vals = [grid[r][c] for r, c in coords]
            shift = k % len(vals)
            vals = vals[shift:] + vals[:shift]

            for (r, c), v in zip(coords, vals):
                grid[r][c] = v

        return grid
