from collections import defaultdict

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maxNumberOfFamilies(*test_input)

    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        # 行 -> 该行列2~9的占用位（列号即二进制位号）
        row_mask = defaultdict(int)
        for r, s in reservedSeats:
            row_mask[r] |= 1 << s

        left = 0b111100       # 列 2,3,4,5
        mid = 0b11110000      # 列 4,5,6,7
        right = 0b1111000000  # 列 6,7,8,9

        ans = 2 * (n - len(row_mask))  # 完全无预定的行各放 2 组
        for mask in row_mask.values():
            if (mask & left == 0) and (mask & right == 0):
                ans += 2
            elif (mask & left == 0) or (mask & right == 0) or (mask & mid == 0):
                ans += 1
        return ans
