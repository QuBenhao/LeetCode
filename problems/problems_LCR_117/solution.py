import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.numSimilarGroups(test_input)

    def numSimilarGroups(self, strs: List[str]) -> int:
        class UnionFind:
            def __init__(self, size):
                self.parent = list(range(size))
                self.rank = [1] * size

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
                return True

            def is_connected(self, x, y):
                return self.find(x) == self.find(y)

        def is_similar(s1, s2):
            diff = 0
            for a, b in zip(s1, s2):
                if a != b:
                    diff += 1
                    if diff > 2:
                        return False
            return diff == 2 or diff == 0

        n = len(strs)
        uf = UnionFind(n)
        for i in range(n):
            for j in range(i + 1, n):
                if is_similar(strs[i], strs[j]):
                    uf.union(i, j)

        return sum(uf.find(i) == i for i in range(n))

