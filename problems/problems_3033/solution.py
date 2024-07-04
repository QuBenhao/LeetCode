import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.modifiedMatrix(test_input)

    def modifiedMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0])
        for j in range(n):
            mx = 0
            remain = []
            for i in range(m):
                if matrix[i][j] == -1:
                    remain.append(i)
                    continue
                mx = max(mx, matrix[i][j])
            for i in remain:
                matrix[i][j] = mx
        return matrix
