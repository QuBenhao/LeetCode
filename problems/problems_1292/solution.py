import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maxSideLength(*test_input)

    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        m, n = len(mat), len(mat[0])
        pre_sum = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                pre_sum[i + 1][j + 1] = pre_sum[i + 1][j] + pre_sum[i][j + 1] - pre_sum[i][j] + mat[i][j]
        ans = 0
        for i in range(m):
            if i < ans:
                continue
            for j in range(ans, n):
                if j < ans:
                    continue
                while ans <= i and ans <= j and pre_sum[i + 1][j + 1] - pre_sum[i + 1][j - ans] - pre_sum[i - ans][
                    j + 1] + pre_sum[i - ans][j - ans] <= threshold:
                    ans += 1
        return ans
