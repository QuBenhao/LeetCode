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
        # 还原原数组 - 方法1：直接计算前缀和
        for i in range(n):
            for j in range(n):
                # 当前位置的值
                ans[i][j] = diff[i][j]
                # 加上左边的值
                if i > 0:
                    ans[i][j] += ans[i - 1][j]
                # 加上上边的值
                if j > 0:
                    ans[i][j] += ans[i][j - 1]
                # 减去左上角的值（因为加了两次）
                if i > 0 and j > 0:
                    ans[i][j] -= ans[i - 1][j - 1]

        return ans
