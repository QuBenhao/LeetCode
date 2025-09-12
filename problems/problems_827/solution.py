import copy

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.largestIsland(test_input)

    def largestIsland(self, grid: List[List[int]]) -> int:
        DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        def point_to_idx(x, y):
            return x * n + y

        n = len(grid)
        uf = UnionFind(n * n)
        for i, row in enumerate(grid):
            for j, val in enumerate(row):
                if val == 1:
                    p = point_to_idx(i, j)
                    for dx, dy in DIRS:
                        if 0 <= (nx := i + dx) < n and 0 <= (ny := j + dy) < n and grid[nx][ny] == 1:
                            uf.union(p, point_to_idx(nx, ny))
        ans = max(uf.size)
        for i, row in enumerate(grid):
            for j, val in enumerate(row):
                if val == 0:
                    tot = 1
                    explored = set()
                    for dx, dy in DIRS:
                        if 0 <= (nx := i + dx) < n and 0 <= (ny := j + dy) < n and grid[nx][ny] == 1:
                            root = uf.find(point_to_idx(nx, ny))
                            if root in explored:
                                continue
                            explored.add(root)
                            tot += uf.size[root]
                    ans = max(ans, tot)

        return ans

class UnionFind:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.rank = [1] * n
        self.size = [1] * n
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
            return False  # 已经在同一集合

        # 按秩合并
        if self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
            self.size[root_x] += self.size[root_y]
        else:
            self.parent[root_x] = root_y
            if self.rank[root_x] == self.rank[root_y]:
                self.rank[root_y] += 1
            self.size[root_y] += self.size[root_x]
        self.cc -= 1
        return True

    def is_connected(self, x:int, y:int) -> bool:
        return self.find(x) == self.find(y)
