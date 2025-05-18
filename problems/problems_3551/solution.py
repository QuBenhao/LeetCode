import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minSwaps(test_input)

    def minSwaps(self, nums: List[int]) -> int:
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

        def sum_num(num):
            return sum(map(int, str(num)))

        target = sorted(nums, key=lambda x: (sum_num(x), x))
        idx_map = {num: i for i, num in enumerate(target)}
        uf = UnionFind(len(nums))
        for i, num in enumerate(nums):
            if num != target[i]:
                uf.union(i, idx_map[num])
        return sum(uf.find(i) != i for i in range(len(nums)))
