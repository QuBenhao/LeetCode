import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minMalwareSpread(*test_input)

    def minMalwareSpread(self, graph: List[List[int]], initial: List[int]) -> int:
        st = set(initial)
        vis = [False] * len(graph)
        def dfs(x: int) -> None:
            vis[x] = True
            nonlocal node_id, size
            size += 1
            # 按照状态机更新 node_id
            if node_id != -2 and x in st:
                node_id = x if node_id == -1 else -2
            for y, conn in enumerate(graph[x]):
                if conn and not vis[y]:
                    dfs(y)

        ans = -1
        max_size = 0
        for x in initial:
            if vis[x]:
                continue
            node_id = -1
            size = 0
            dfs(x)
            if node_id >= 0 and (size > max_size or size == max_size and node_id < ans):
                ans = node_id
                max_size = size
        return min(initial) if ans < 0 else ans
