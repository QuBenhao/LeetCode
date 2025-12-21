from collections import defaultdict

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.interactionCosts(*test_input)

    def interactionCosts(self, n: int, edges: List[List[int]], group: List[int]) -> int:
        graph = [[] for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        ans = 0
        def dfs(node, pa):
            nonlocal ans
            cur = defaultdict(lambda: [0, 0])
            for child in graph[node]:
                if child != pa:
                    child_dict = dfs(child, node)
                    for k, v in child_dict.items():
                        # 子树到当前节点,每个节点都要增加1距离，故增加节点个数
                        v[1] += v[0]
                        # 累加当前组对答案的最终贡献, 这种情况是折线。
                        if cur[k][0]:
                            ans += cur[k][1] * v[0] + cur[k][0] * v[1]
                        # 合并到当前节点统计
                        cur[k][0] += v[0]
                        cur[k][1] += v[1]
            # 所有子树和当前节点的组合的贡献和
            ans += cur[group[node]][1]
            # 加入当前node的分组统计
            cur[group[node]][0] += 1
            return cur

        dfs(0, -1)
        return ans
