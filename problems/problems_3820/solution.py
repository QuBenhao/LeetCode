import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.specialNodes(*test_input)

    def specialNodes(self, n: int, edges: List[List[int]], x: int, y: int, z: int) -> int:
        g = [[] for _ in range(n)]
        for u, v in edges:  # Nodes are numbered from 0
            g[u].append(v)
            g[v].append(u)
        ta = TreeAncestor(n, g)

        def check(p) -> int:
            a, b, c = ta.get_dis(p, x), ta.get_dis(p, y), ta.get_dis(p, z)
            s = a + b + c
            a, c = min(a, b, c), max(a, b, c)
            b = s - a - c
            return 1 if a * a + b * b == c * c else 0

        def dfs(node, fa: int) -> int:
            ans = check(node)
            for child in g[node]:
                if child != fa:
                    ans += dfs(child, node)
            return ans

        return dfs(0, -1)


class TreeAncestor:
    def __init__(self, n, g):
        m = n.bit_length()

        depth = [0] * n
        pa = [[-1] * m for _ in range(n)]

        def dfs(x: int, fa: int) -> None:
            pa[x][0] = fa
            for y in g[x]:
                if y != fa:
                    depth[y] = depth[x] + 1
                    dfs(y, x)

        dfs(0, -1)

        for i in range(m - 1):
            for x in range(n):
                if (p := pa[x][i]) != -1:
                    pa[x][i + 1] = pa[p][i]
        self.depth = depth
        self.pa = pa

    def get_kth_ancestor(self, node: int, k: int) -> int:
        for i in range(k.bit_length()):
            if k >> i & 1:  # Bit i of k, counted from least to most significant, is 1
                node = self.pa[node][i]
        return node

    # Return the lowest common ancestor of x and y (nodes are numbered from 0)
    def get_lca(self, x: int, y: int) -> int:
        if self.depth[x] > self.depth[y]:
            x, y = y, x
        # Bring y to the same depth as x
        y = self.get_kth_ancestor(y, self.depth[y] - self.depth[x])
        if y == x:
            return x
        for i in range(len(self.pa[x]) - 1, -1, -1):
            px, py = self.pa[x][i], self.pa[y][i]
            if px != py:
                x, y = px, py  # Jump upward 2**i steps together
        return self.pa[x][0]

    def get_dis(self, x: int, y: int) -> int:
        return self.depth[x] + self.depth[y] - self.depth[self.get_lca(x, y)] * 2
