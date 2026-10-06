import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minSwaps(test_input)

    def minSwaps(self, grid: List[List[int]]) -> int:
        # Precompute the number of trailing zeros in each row
        n = len(grid)
        tail_zeros = [n] * n
        for i in range(n):
            for j in range(n - 1, -1, -1):
                if grid[i][j]:
                    tail_zeros[i] = n - 1 - j
                    break

        ans = 0
        for i in range(n - 1):
            need_zeros = n - 1 - i
            for j in range(i, n):
                if tail_zeros[j] >= need_zeros:
                    ans += j - i
                    # Move j to i, shifting the original entries in [i, j-1] one position right
                    tail_zeros[i + 1: j + 1] = tail_zeros[i: j]
                    break
            else:  # No suitable tail_zeros[j] was found
                return -1
        return ans
