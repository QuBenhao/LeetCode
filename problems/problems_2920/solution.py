from functools import cache

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maximumPoints(*test_input)

    def maximumPoints(self, edges: List[List[int]], coins: List[int], k: int) -> int:
        g = [[] for _ in coins]
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)

        @cache  # Cache decorator to avoid recomputing dfs results (memoization)
        def dfs(i: int, j: int, fa: int) -> int:
            res1 = (coins[i] >> j) - k
            res2 = coins[i] >> (j + 1)
            for ch in g[i]:
                if ch != fa:
                    res1 += dfs(ch, j, i)  # Do not shift right
                    if j < 13:  # j+1 >= 14 is equivalent to res2 += 0, so no recursion is needed
                        res2 += dfs(ch, j + 1, i)  # Shift right
            return max(res1, res2)

        return dfs(0, 0, -1)
