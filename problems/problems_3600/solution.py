from bisect import bisect_left

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maxStability(*test_input)

    def maxStability(self, n: int, edges: List[List[int]], k: int) -> int:
        must_edges = []
        avail_edges = []
        all_uf = UnionFind(n)
        uf = UnionFind(n)
        right = 200000
        for u, v, s, must in edges:
            if must:
                must_edges.append((u, v, s))
                if not uf.union(u, v):
                    return -1  # 必选边成环
                right = min(right, s)
            else:
                avail_edges.append((u, v, s))
            all_uf.union(u, v)

        avail_edges.sort(key=lambda x: x[2])

        def helper(strength):
            cur_k = k
            cur_uf = uf.__copy__()
            length = len(avail_edges)
            free_idx = bisect_left(range(length), strength, key=lambda x: avail_edges[x][2])
            for fi in range(free_idx, length):
                u, v, s = avail_edges[fi]
                if cur_uf.union(u, v):
                    if cur_uf.size == 1:
                        return True
            double_idx = bisect_left(range(length), (strength + 1) // 2, key=lambda x: avail_edges[x][2])
            for di in range(double_idx, free_idx):
                if cur_k <= 0:
                    break
                u, v, s = avail_edges[di]
                if cur_uf.union(u, v):
                    cur_k -= 1
                    if cur_uf.size == 1:
                        return True
            return cur_uf.size == 1

        if all_uf.size > 1:
            return -1  # 无法连通

        left = 1
        while left < right:
            mid = (left + right + 1) // 2
            if helper(mid):
                left = mid
            else:
                right = mid - 1
        return left


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

    def __copy__(self):
        new_uf = UnionFind(len(self.parent))
        new_uf.parent = self.parent[:]
        new_uf.rank = self.rank[:]
        new_uf.size = self.size
        return new_uf
