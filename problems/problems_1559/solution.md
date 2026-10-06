# 1559. Detect Cycles in 2D Grid

[Problem link](https://leetcode.cn/problems/detect-cycles-in-2d-grid/description/)

[TOC]

# Intuition

> Union-find

Determine whether the grid contains a cycle of **equal characters** with length >= 4. Key observations:

1. **Only horizontal/vertical moves are allowed** -> the smallest cycle is a 2×2 square (4 cells).
2. **Only equal characters can connect** -> consider only adjacent cells with the same character.
3. **Cycle detection**: if two adjacent cells are **already connected** when we try to merge them, adding this edge forms a cycle.

Since the minimum cycle length is 4, detecting an existing connection guarantees the length requirement is met.

# Solution steps

1. **Coordinate mapping**: map the 2D coordinates `(i, j)` to the 1D index `i * n + j`.
2. **Traversal order**: for each cell, check only its **right** and **bottom** neighbors to avoid processing an edge twice.
3. **Union-find merge**:
   - If adjacent cells contain the same character, try to merge them.
   - If `union` returns `False` (already in the same set), a cycle has formed; return `True`.
4. **After traversal**: return `False` if no cycle was found.

# Complexity

- Time complexity: $O(m \times n \times \alpha(mn))$, where $\alpha$ is the inverse Ackermann function, effectively constant in practice.
- Space complexity: $O(m \times n)$

# Code
```Python3 []
class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        m, n = len(grid), len(grid[0])

        def to_idx(x, y):
            return x * n + y

        uf = UnionFind(m * n)
        for i in range(m):
            for j in range(n):
                idx = to_idx(i, j)
                if j < n - 1 and grid[i][j] == grid[i][j + 1]:
                    nxt = to_idx(i, j + 1)
                    if not uf.union(idx, nxt):
                        return True
                if i < m - 1 and grid[i][j] == grid[i + 1][j]:
                    nxt = to_idx(i + 1, j)
                    if not uf.union(idx, nxt):
                        return True
        return False


class UnionFind:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.rank = [1] * n

    def find(self, x: int) -> int:
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, x: int, y: int) -> bool:
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return False

        if self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_x] = root_y
            if self.rank[root_x] == self.rank[root_y]:
                self.rank[root_y] += 1
        return True
```
