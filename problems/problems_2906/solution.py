import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.constructProductMatrix(test_input)

    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        MOD = 12345
        n, m = len(grid), len(grid[0])
        total = n * m
        # 只用前缀数组，后缀用滚动变量
        pre = [1] * total
        for i in range(n):
            for j in range(m):
                idx = i * m + j
                pre[idx] = pre[idx - 1] * grid[i][j] % MOD if idx > 0 else grid[i][j] % MOD

        ans = [[0] * m for _ in range(n)]
        suf = 1
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                idx = i * m + j
                p = pre[idx - 1] if idx > 0 else 1
                ans[i][j] = p * suf % MOD
                suf = suf * grid[i][j] % MOD
        return ans
