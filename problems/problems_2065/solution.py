import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maximalPathQuality(*test_input)

    def maximalPathQuality(self, values: List[int], edges: List[List[int]], max_time: int) -> int:
        n = len(values)
        g = [[] for _ in range(n)]
        for x, y, t in edges:
            g[x].append((y, t))
            g[y].append((x, t))

        def dfs(x: int, sum_time: int, sum_value: int) -> None:
            if x == 0:
                nonlocal ans
                ans = max(ans, sum_value)
                # Do not return here; the walk can continue
            for y, t in g[x]:
                if sum_time + t > max_time:
                    continue
                if vis[y]:
                    dfs(y, sum_time + t, sum_value)
                else:
                    vis[y] = True
                    # Count each node's value at most once in the total
                    dfs(y, sum_time + t, sum_value + values[y])
                    vis[y] = False  # Restore the previous state

        ans = 0
        vis = [False] * n
        vis[0] = True
        dfs(0, 0, values[0])
        return ans
