# [Python] DFS

> Author: Benhao
> Date: 2024-03-02
> Upvotes: 1
> Tags: C, Go, Java, Python3, TypeScript

---


> Problem: [200. 岛屿数量](https://leetcode.cn/problems/number-of-islands/description/)

[TOC]

# Intuition

> Use multi-source DFS, recording visited cells to determine connectivity.

# Approach

> Multi-source DFS

# Complexity

Time complexity:
> $O(mn)$

Space complexity:
> $O(mn)$



# Code
```Python3 []
DIRS = [(-1, 0), (0, 1), (0, -1), (1, 0)]
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        explored = set()
        
        def dfs(x, y):
            if (x, y) in explored:
                return 0
            explored.add((x, y))
            ans = 1
            for dx, dy in DIRS:
                if (nx := x + dx) >= 0 and nx < m and (ny := y + dy) >= 0 and ny < n and grid[nx][ny] == "1":
                    ans += dfs(nx, ny)
            return ans
        
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    ans += dfs(i, j) > 0
        return ans
```
  
