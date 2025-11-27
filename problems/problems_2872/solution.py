import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maxKDivisibleComponents(*test_input)

    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        g = [[] for _ in range(n)]
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)

        # 返回子树 x 的点权和
        def dfs(x: int, fa: int) -> int:
            s = values[x]
            for y in g[x]:
                if y != fa:  # 避免访问父节点
                    # 加上子树 y 的点权和，得到子树 x 的点权和
                    s += dfs(y, x)
            nonlocal ans
            ans += s % k == 0
            return s

        ans = 0
        dfs(0, -1)
        return ans
