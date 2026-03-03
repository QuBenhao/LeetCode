import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.numSpecial(test_input)

    def numSpecial(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        sum_rows, sum_cols = [0] * m, [0] * n
        check = set()
        for i, row in enumerate(mat):
            for j, val in enumerate(row):
                if val == 0:
                    continue
                sum_rows[i] += val
                sum_cols[j] += val
                check.add((i, j))
        return sum(sum_rows[i] == sum_cols[j] == 1 for i, j in check)
