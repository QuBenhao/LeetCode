from math import inf

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minScore(*test_input)

    def minScore(self, n: int, roads: List[List[int]]) -> int:
        g = [[] for _ in range(n + 1)]
        for x, y, dis in roads:
            g[x].append((y, dis))
            g[y].append((x, dis))

        vis = [False] * (n + 1)
        ans = inf

        def dfs(x: int) -> None:
            nonlocal ans
            vis[x] = True  # 避免重复访问
            for y, dis in g[x]:
                ans = min(ans, dis)
                if not vis[y]:
                    dfs(y)

        # 遍历节点 1 所在连通块
        dfs(1)
        return ans
