from math import inf

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maxMatrixSum(test_input)

    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        ans = 0
        neg_cnt = 0
        min_val = inf
        for row in matrix:
            for v in row:
                if v < 0:
                    neg_cnt += 1
                min_val = min (min_val, abs(v))
                ans += abs(v)
        return ans if neg_cnt % 2 == 0 else ans - 2 * min_val
