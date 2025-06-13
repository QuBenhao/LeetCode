import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.pathExistenceQueries(*test_input)

    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
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
        
        uf = UnionFind(n)
        for i in range(n - 1):
            if abs(nums[i] - nums[i + 1]) <= maxDiff:
                uf.union(i, i + 1)
        results = [False] * len(queries)
        for i, (u, v) in enumerate(queries):
            results[i] = uf.is_connected(u, v)
        return results
