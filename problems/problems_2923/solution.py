import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.findChampion(test_input)

    def findChampion(self, grid: List[List[int]]) -> int:
        for i, row in enumerate(grid):
            if all(i == j or v == 1 for j, v in enumerate(row)):
                return i
        return -1