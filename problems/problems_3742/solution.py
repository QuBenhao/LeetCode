from math import inf

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maxPathScore(*test_input)

    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        # dp[i][j] 存储 {花费: 最大得分}
        # 花费: 非零单元格各花费1
        dp = [[{} for _ in range(n)] for _ in range(m)]
        dp[0][0][0] = 0  # 起点，花费0，得分0

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                score, cost = grid[i][j], 1 if grid[i][j] else 0
                cur = {}
                if i > 0:
                    for c, val in dp[i - 1][j].items():
                        if c + cost <= k:
                            cur[c + cost] = max(cur.get(c + cost, -inf), val + score)
                if j > 0:
                    for c, val in dp[i][j - 1].items():
                        if c + cost <= k:
                            cur[c + cost] = max(cur.get(c + cost, -inf), val + score)
                dp[i][j] = cur

        return -1 if not dp[m - 1][n - 1] else max(dp[m - 1][n - 1].values())
