import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.numMagicSquaresInside(test_input)

    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        ans = 0
        for i in range(1, m - 1):
            for j in range(1, n - 1):
                if grid[i][j] != 5:
                    continue

                mask = 0
                r_sum = [0] * 3
                c_sum = [0] * 3
                for r in range(i - 1, i + 2):
                    for c in range(j - 1, j + 2):
                        x = grid[r][c]
                        mask |= 1 << x
                        r_sum[r - i + 1] += x
                        c_sum[c - j + 1] += x

                # 1 ~ 9 = 1111111110 = 2^10 - 2
                if mask == 1022 and all(r == 15 for r in r_sum) and all(c == 15 for c in c_sum):
                    ans += 1
        return ans
