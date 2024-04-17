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
                    # 按照 924 题的状态机更新 node_id
                    # 注意避免重复统计，例如上图中的 0 有两条不同路径可以遇到 1
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
            if node_id >= 0:  # 只找到一个在 initial 中的节点
                # 删除节点 node_id 可以让 size 个点不被感染
                cnt[node_id] += size

        # size 取反计算最大值，相同最大值取 node_id 最小值
        return min((-size, node_id) for node_id, size in cnt.items())[1] if cnt else min(initial)
