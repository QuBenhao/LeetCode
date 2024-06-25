import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.goodSubsetofBinaryMatrix(test_input)


    def goodSubsetofBinaryMatrix(self, grid: List[List[int]]) -> List[int]:
        mask_to_idx = {}
        for i, row in enumerate(grid):
            mask = 0
            for j, x in enumerate(row):
                mask |= x << j
            if mask == 0:
                return [i]
            mask_to_idx[mask] = i

        for x, i in mask_to_idx.items():
            for y, j in mask_to_idx.items():
                if (x & y) == 0:
                    return sorted((i, j))
        return []

