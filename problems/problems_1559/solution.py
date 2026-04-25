import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.containsCycle(test_input)

    def containsCycle(self, grid: List[List[str]]) -> bool:
        m, n = len(grid), len(grid[0])

        def to_idx(x, y):
            return x * n + y

        uf = UnionFind(m * n)
        for i in range(m):
            for j in range(n):
                idx = to_idx(i, j)
                # 只检查右边和下边，避免重复
                if j < n - 1 and grid[i][j] == grid[i][j + 1] and not uf.union(idx, idx + 1):
                    return True
                if i < m - 1 and grid[i][j] == grid[i + 1][j] and not uf.union(idx, idx + n):
                    return True
        return False


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
