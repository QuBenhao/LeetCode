import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.countCompleteComponents(*test_input)

    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)
        for a, b in edges:
            uf.union(a, b)
        return sum(uf.links[i] * 2 == uf.size[i] * (uf.size[i] - 1) for i in range(n) if uf.find(i) == i)


class UnionFind:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.rank = [1] * n
        self.size = [1] * n
        self.links = [0] * n
        self.cc = n

    def find(self, x: int) -> int:
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]  # 路径压缩
            x = self.parent[x]
        return x

    def union(self, x: int, y: int) -> bool:
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            self.links[root_x] += 1
            return False  # 已经在同一集合

        # 按秩合并
        if self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
            self.size[root_x] += self.size[root_y]
            self.links[root_x] += self.links[root_y] + 1
        else:
            self.parent[root_x] = root_y
            if self.rank[root_x] == self.rank[root_y]:
                self.rank[root_y] += 1
            self.size[root_y] += self.size[root_x]
            self.links[root_y] += self.links[root_x] + 1
        self.cc -= 1
        return True

    def is_connected(self, x:int, y:int) -> bool:
        return self.find(x) == self.find(y)
