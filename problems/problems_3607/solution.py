from collections import defaultdict

from sortedcontainers import SortedSet

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.processQueries(*test_input)

    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        uf = UnionFind(c)
        for u, v in connections:
            uf.union(u - 1, v - 1)
        online = defaultdict(lambda: SortedSet())
        for i in range(c):
            online[uf.find(i)].add(i)
        ans = []
        for op, x in queries:
            root = uf.find(x - 1)
            if op == 2:
                online[root].discard(x - 1)
            else:
                if not online[root]:
                    ans.append(-1)
                else:
                    ans.append(online[root][0] + 1 if x - 1 not in online[root] else x)
        return ans

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
