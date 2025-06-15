import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.findMedian(*test_input)

    def findMedian(self, n: int, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        ta = TreeAncestor(edges)
        ans = [-1] * len(queries)
        for i, (u, v) in enumerate(queries):
            if u == v:
                ans[i] = u
                continue
            lca = ta.get_lca(u, v)
            total_dis = ta.distance[u] + ta.distance[v] - 2 * ta.distance[lca]
            cur = ta.distance[u] - ta.distance[lca]
            half_dis = (total_dis + 1) // 2
            if cur >= half_dis:
                # 如果 u 到 lca 的距离大于等于半条路径长度，则中位数在 u 到 lca 之间
                x = ta.find_distance(u, half_dis-1)
                x = ta.pa[x][0] # 找到 x 的父节点, 因为x 是 刚好不够, 其父节点是答案
            else:
                # 如果 u 到 lca 的距离小于半条路径长度，则中位数在 v 到 lca 之间
                x = ta.find_distance(v, total_dis - half_dis)
            ans[i] = x
        return ans


class TreeAncestor:
    def __init__(self, edges: List[List[int]]):
        n = len(edges) + 1
        m = n.bit_length()
        g = [[] for _ in range(n)]
        for x, y, w in edges:  # 节点编号从 0 开始
            g[x].append((y, w))
            g[y].append((x, w))

        depth = [0] * n
        distance = [0] * n
        pa = [[-1] * m for _ in range(n)]

        def dfs(x: int, fa: int) -> None:
            pa[x][0] = fa
            for (y, w) in g[x]:
                if y != fa:
                    depth[y] = depth[x] + 1
                    distance[y] = distance[x] + w
                    dfs(y, x)

        dfs(0, -1)

        for i in range(m - 1):
            for x in range(n):
                if (p := pa[x][i]) != -1:
                    pa[x][i + 1] = pa[p][i]

        self.m = m
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

    def find_distance(self, x: int, d: int):
        d = self.distance[x] - d
        for i in range(self.m-1, -1, -1):
            if (p := self.pa[x][i]) != -1 and self.distance[p] >= d:
                x = p
        return x
