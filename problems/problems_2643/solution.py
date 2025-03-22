import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.rowAndMaximumOnes(test_input)

    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        ans = [0, 0]
        for i, row in enumerate(mat):
            cur = sum(row)
            if cur > ans[1]:
                ans[0], ans[1] = i, cur
        return ans
