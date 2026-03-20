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
                # 收集 k x k 子矩阵中的所有元素
                vals = []
                for x in range(i, i + k):
                    for y in range(j, j + k):
                        vals.append(grid[x][y])

                # 排序后找最小相邻差
                vals.sort()
                min_diff = 0
                for t in range(1, len(vals)):
                    if vals[t] != vals[t - 1]:
                        diff = vals[t] - vals[t - 1]
                        if min_diff == 0 or diff < min_diff:
                            min_diff = diff

                ans[i][j] = min_diff

        return ans

