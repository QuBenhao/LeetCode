from bisect import bisect_right

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.countNegatives(test_input)

    def countNegatives(self, grid: List[List[int]]) -> int:
        # ans = 0
        # n, m = len(grid), len(grid[0])
        # cur_right = m
        # for i, row in enumerate(grid):
        #     idx = bisect_right(row, 0, hi=cur_right, key=lambda x: -x)
        #     ans += (cur_right - idx) * (n - i)
        #     cur_right = idx
        # return ans

        ans = 0
        n, m = len(grid), len(grid[0])
        i, j = 0, m - 1
        while i < n and j >= 0:
            if grid[i][j] < 0:
                ans += n - i
                j -= 1
            else:
                i += 1
        return ans
