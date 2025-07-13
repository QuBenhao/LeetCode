import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minCost(*test_input)

    def minCost(self, n: int, edges: List[List[int]], k: int) -> int:
        uf = UnionFind(n)
        if k == n:
            return 0
        for u, v, w in sorted(edges, key=lambda x: x[2]):
            uf.union(u, v)
            if uf.size == k:
                return w
        return 0


class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [1] * size
        self.size = size

    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]  # 路径压缩
            x = self.parent[x]
        return x

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return False  # 已经在同一集合

        # 按秩合并
        if self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_x] = root_y
            if self.rank[root_x] == self.rank[root_y]:
                self.rank[root_y] += 1
        self.size -= 1
        return True

    def is_connected(self, x, y):
        return self.find(x) == self.find(y)
