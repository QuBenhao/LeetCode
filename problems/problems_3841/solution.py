import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.palindromePath(*test_input)

    def palindromePath(self, n: int, edges: list[list[int]], s: str, queries: list[str]) -> list[bool]:
        g = [[] for _ in range(n)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        # 迭代 DFS：求父节点、深度、先序时间戳（子树连续）
        parent = [0] * n
        depth = [0] * n
        tin = [0] * n
        order = []
        stack = [0]
        parent[0] = 0
        while stack:
            u = stack.pop()
            tin[u] = len(order)
            order.append(u)
            for v in g[u]:
                if v != parent[u]:
                    parent[v] = u
                    depth[v] = depth[u] + 1
                    stack.append(v)

        size = [1] * n
        for u in reversed(order[1:]):
            size[parent[u]] += size[u]

        # rx0[u]：初始根到 u 的掩码异或
        rx0 = [0] * n
        rx0[0] = 1 << (ord(s[0]) - 97)
        for u in order[1:]:
            rx0[u] = rx0[parent[u]] ^ (1 << (ord(s[u]) - 97))

        # 倍增 LCA
        log = max(1, n.bit_length())
        up = [parent]
        for _ in range(1, log):
            prev = up[-1]
            up.append([prev[prev[v]] for v in range(n)])

        def lca(a, b):
            if depth[a] < depth[b]:
                a, b = b, a
            diff = depth[a] - depth[b]
            k = 0
            while diff:
                if diff & 1:
                    a = up[k][a]
                diff >>= 1
                k += 1
            if a == b:
                return a
            for k in range(log - 1, -1, -1):
                if up[k][a] != up[k][b]:
                    a, b = up[k][a], up[k][b]
            return up[0][a]

        # 树状数组维护「区间异或 + 单点查询」，只存相对 rx0 的增量
        bit = [0] * (n + 1)

        def add(i, val):
            i += 1
            while i <= n:
                bit[i] ^= val
                i += i & -i

        def pref(i):
            i += 1
            res = 0
            while i:
                res ^= bit[i]
                i -= i & -i
            return res

        def cur_rx(u):
            return rx0[u] ^ pref(tin[u])

        ans = []
        for q in queries:
            op, a, b = q.split()
            u = int(a)
            if op == 'update':
                delta = (1 << (ord(s[u]) - 97)) ^ (1 << (ord(b) - 97))
                if delta:
                    add(tin[u], delta)
                    if tin[u] + size[u] < n:
                        add(tin[u] + size[u], delta)
                    s = s[:u] + b + s[u + 1:]
            else:
                v = int(b)
                w = lca(u, v)
                m = cur_rx(u) ^ cur_rx(v) ^ (1 << (ord(s[w]) - 97))
                ans.append(m & (m - 1) == 0)
        return ans

