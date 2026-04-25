# 1559. 二维网格图中探测环

[题目链接](https://leetcode.cn/problems/detect-cycles-in-2d-grid/description/)

[TOC]

# 思路

> 并查集

题目要求检测网格中是否存在由**相同字符**构成的环（长度 ≥ 4）。关键观察：

1. **只能水平/垂直移动** → 最小的环是 2×2 的正方形（4 个格子）
2. **相同字符才能相连** → 只需考虑同字符的相邻格子
3. **环的判定**：如果在合并两个相邻格子的过程中发现它们**已经连通**，说明添加这条边会形成环

由于最小环长度为 4，一旦发现已连通，必然满足环长度要求。

# 解题过程

1. **坐标映射**：将二维坐标 `(i, j)` 映射为一维索引 `i * n + j`
2. **遍历顺序**：对于每个格子，只检查**右边**和**下边**的相邻格子（避免重复处理）
3. **并查集合并**：
   - 如果相邻格子字符相同，尝试合并
   - 若 `union` 返回 `False`（已在同一集合），说明形成环，返回 `True`
4. **遍历完成**：若无环，返回 `False`

# 复杂度

- 时间复杂度: $O(m \times n \times \alpha(mn))$，其中 $\alpha$ 是反阿克曼函数，实际接近常数
- 空间复杂度: $O(m \times n)$

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
