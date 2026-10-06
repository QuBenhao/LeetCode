import solution
from typing import List


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.rotateGrid(*test_input)

    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        # Directions: right, down, left, up (counterclockwise)
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        for layer in range(min(m, n) // 2):
            top, left = layer, layer
            bottom, right = m - 1 - layer, n - 1 - layer
            # Length of each side
            lengths = [right - left, bottom - top, right - left, bottom - top]

            # Generate this layer's coordinates in counterclockwise order
            coords = []
            i, j = top, left
            for (di, dj), length in zip(dirs, lengths):
                for _ in range(length):
                    coords.append((i, j))
                    i += di
                    j += dj

            # Extract, rotate, and write back
            vals = [grid[r][c] for r, c in coords]
            shift = k % len(vals)
            vals = vals[shift:] + vals[:shift]

            for (r, c), v in zip(coords, vals):
                grid[r][c] = v

        return grid
