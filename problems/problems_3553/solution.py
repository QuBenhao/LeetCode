from collections import defaultdict

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minimumWeight(*test_input)

    def minimumWeight(self, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        class TreeAncestor:
            def __init__(self, edges: List[List[int]]):
                n = len(edges) + 1
                m = n.bit_length()
                graph = defaultdict(list)
                for x, y, w in edges:  # 节点编号从 0 开始
                    graph[x].append((y, w))
                    graph[y].append((x, w))

                depth = [0] * n
                pa = [[-1] * m for _ in range(n)]
                distance = [0] * n

                def dfs(x: int, fa: int) -> None:
                    pa[x][0] = fa
                    for y, w in graph[x]:
                        if y != fa:
                            depth[y] = depth[x] + 1
                            distance[y] = distance[x] + w
                            dfs(y, x)

                dfs(0, -1)

                for i in range(m - 1):
                    for x in range(n):
                        if (p := pa[x][i]) != -1:
                            pa[x][i + 1] = pa[p][i]
                self.depth = depth
                self.pa = pa
                self.distance = distance

            def get_kth_ancestor(self, node: int, k: int) -> int:
                for i in range(k.bit_length()):
                    if k >> i & 1:  # k 二进制从低到高第 i 位是 1
                        node = self.pa[node][i]
                return node

            # 返回 x 和 y 的最近公共祖先（节点编号从 0 开始）
            def get_lca(self, x: int, y: int) -> int:
                if self.depth[x] > self.depth[y]:
                    x, y = y, x
                # 使 y 和 x 在同一深度
                y = self.get_kth_ancestor(y, self.depth[y] - self.depth[x])
                if y == x:
                    return x
                for i in range(len(self.pa[x]) - 1, -1, -1):
                    px, py = self.pa[x][i], self.pa[y][i]
                    if px != py:
                        x, y = px, py  # 同时往上跳 2**i 步
                return self.pa[x][0]

            def get_distance(self, x: int, y: int) -> int:
                return self.distance[x] + self.distance[y] - 2 * self.distance[self.get_lca(x, y)]

        tc = TreeAncestor(edges)
        ans = [0] * len(queries)
        for i, (src1, src2, dest) in enumerate(queries):
            ans[i] = (tc.get_distance(src1, dest) + tc.get_distance(src2, dest) + tc.get_distance(src1, src2)) // 2
        return ans
