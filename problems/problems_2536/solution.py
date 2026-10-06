import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.rangeAddQueries(*test_input)

    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        diff = [[0] * (n + 1) for _ in range(n + 1)]
        for x1, y1, x2, y2 in queries:
            diff[x1][y1] += 1
            diff[x1][y2+1] -= 1
            diff[x2+1][y1] -= 1
            diff[x2+1][y2+1] += 1
        ans = [[0] * n for _ in range(n)]
        # Reconstruct the original array - method 1: compute prefix sums directly
        for i in range(n):
            for j in range(n):
                # Value at the current position
                ans[i][j] = diff[i][j]
                # Add the value to the left
                if i > 0:
                    ans[i][j] += ans[i - 1][j]
                # Add the value above
                if j > 0:
                    ans[i][j] += ans[i][j - 1]
                # Subtract the top-left value (it was added twice)
                if i > 0 and j > 0:
                    ans[i][j] -= ans[i - 1][j - 1]

        return ans
