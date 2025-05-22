from collections import defaultdict

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.longestConsecutive(test_input)

    def longestConsecutive(self, nums: List[int]) -> int:
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

        n = len(nums)
        uf = UnionFind(n)
        idx_map = {}
        for i, num in enumerate(nums):
            if num in idx_map:
                continue
            idx_map[num] = i
            if num - 1 in idx_map:
                uf.union(i, idx_map[num - 1])
            if num + 1 in idx_map:
                uf.union(i, idx_map[num + 1])
        ans = 0
        # 统计每个集合的大小
        size_map = defaultdict(int)
        for i in idx_map.values():
            root = uf.find(i)
            size_map[root] += 1
            ans = max(ans, size_map[root])
        return ans
