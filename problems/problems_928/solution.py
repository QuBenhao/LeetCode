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
            for y, conn in enumerate(graph[x]):
                if conn == 0:
                    continue
                if y in st:
                    # Update node_id using the state machine from problem 924
                    # Avoid double counting: for example, 0 in the diagram above can reach 1 along two different paths
                    if node_id != -2 and node_id != y:
                        node_id = y if node_id == -1 else -2
                elif not vis[y]:
                    dfs(y)

        cnt = Counter()
        for i, seen in enumerate(vis):
            if seen or i in st:
                continue
            node_id = -1
            size = 0
            dfs(i)
            if node_id >= 0:  # Found only one node from initial
                # Removing node_id prevents size nodes from being infected
                cnt[node_id] += size

        # Negate size to select the maximum; break ties with the smallest node_id
        return min((-size, node_id) for node_id, size in cnt.items())[1] if cnt else min(initial)
