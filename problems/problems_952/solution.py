import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.largestComponentSize(test_input)

    def largestComponentSize(self, nums: List[int]) -> int:
        prime_to_idx = {}
        n = len(nums)
        uf = UnionFind(n)
        for i, num in enumerate(nums):
            for p in PRIME_FACTORS[num]:
                if p in prime_to_idx:
                    uf.union(i, prime_to_idx[p])
                prime_to_idx[p] = i
        return max(uf.vals)


# 预处理每个数的质因子列表
mx = 100001
PRIME_FACTORS = [[] for _ in range(mx)]
for _i in range(2, mx):
    if not PRIME_FACTORS[_i]:  # i 是质数
        for _j in range(_i, mx, _i):  # i 的倍数有质因子 i
            PRIME_FACTORS[_j].append(_i)

class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [1] * size
        self.vals = [1] * size
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
            self.vals[root_x] += self.vals[root_y]
        else:
            self.parent[root_x] = root_y
            if self.rank[root_x] == self.rank[root_y]:
                self.rank[root_y] += 1
            self.vals[root_y] += self.vals[root_x]
        self.size -= 1
        return True

    def is_connected(self, x, y):
        return self.find(x) == self.find(y)