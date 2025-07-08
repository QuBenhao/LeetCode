import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.canTransform(*test_input)

    def canTransform(self, start: str, result: str) -> bool:
        i, j = 0, 0
        n = len(start)
        while i < n or j < n:
            while i < n and start[i] == 'X':
                i += 1
            while j < n and result[j] == 'X':
                j += 1
            if i == n or j == n:
                return i == j
            if start[i] != result[j]:
                return False
            if start[i] == 'L' and i < j:
                return False
            if start[i] == 'R' and i > j:
                return False
            i += 1
            j += 1
        return i == j
