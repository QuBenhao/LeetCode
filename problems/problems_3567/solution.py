import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minAbsDiff(*test_input)

    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        ans = [[0] * (n - k + 1) for _ in range(m - k + 1)]

        for i in range(m - k + 1):
            for j in range(n - k + 1):
                # Collect all elements in the k x k submatrix
                vals = []
                for x in range(i, i + k):
                    for y in range(j, j + k):
                        vals.append(grid[x][y])

                # Sort and find the minimum difference between adjacent elements
                vals.sort()
                min_diff = 0
                for t in range(1, len(vals)):
                    if vals[t] != vals[t - 1]:
                        diff = vals[t] - vals[t - 1]
                        if min_diff == 0 or diff < min_diff:
                            min_diff = diff

                ans[i][j] = min_diff

        return ans

