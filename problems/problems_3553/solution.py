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

                def dfs(node: int, parent: int):
                    pa[node][0] = parent
                    for (child, weight) in graph[node]:
                        if child != parent:
                            depth[child] = depth[node] + 1
                            distance[child] = distance[node] + weight
                            dfs(child, node)

                dfs(0, -1)
                for j in range(1, m):
                    for i in range(n):
                        if pa[i][j - 1] != -1:
                            pa[i][j] = pa[pa[i][j - 1]][j - 1]
                self.depth = depth
                self.pa = pa
                self.distance = distance

            def get_kth_ancestor(self, node: int, k: int) -> int:
                while k > 0 and node != -1:
                    node = self.pa[node][(k & -k).bit_length() - 1]
                    k &= k - 1
                return node

            # 返回 x 和 y 的最近公共祖先（节点编号从 0 开始）
            def get_lca(self, x: int, y: int) -> int:
                if self.depth[x] > self.depth[y]:
                    x, y = y, x
                # 先将 y 提升到与 x 同一深度
                y = self.get_kth_ancestor(y, self.depth[y] - self.depth[x])
                if y == x:
                    return x
                for i in range(len(self.pa[x]) - 1, -1, -1):
                    if (pa_x := self.pa[x][i]) != (pa_y := self.pa[y][i]):
                        x, y = pa_x, pa_y
                return self.pa[x][0]

            def get_distance(self, x: int, y: int) -> int:
                return self.distance[x] + self.distance[y] - 2 * self.distance[self.get_lca(x, y)]

        tree_ancestor = TreeAncestor(edges)
        result = [0] * len(queries)
        for i, (_x, _y, _d) in enumerate(queries):
            result[i] = (tree_ancestor.get_distance(_x, _y)
                         + tree_ancestor.get_distance(_x, _d)
                         + tree_ancestor.get_distance(_y, _d)) // 2
        return result
