import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.areSimilar(*test_input)

    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        n = len(mat[0])
        for i, row in enumerate(mat):
            for j in range(n):
                if row[(j + (k if i % 2 == 0 else -k)) % n] != row[j]:
                    return False
        return True
