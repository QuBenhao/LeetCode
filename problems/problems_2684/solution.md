# [Python] BFS或DFS

> slug: python-bfshuo-dfs-by-himymben-t19b
> date: 2024-03-16
> tags: C, Go, Java, Python3, TypeScript
> question: Maximum Number of Moves in a Grid (maximum-number-of-moves-in-a-grid)
> url: https://leetcode.cn/problems/maximum-number-of-moves-in-a-grid/solutions/vOlfJX/python-bfshuo-dfs-by-himymben-t19b/

---

> Problem: [2684. 矩阵中移动的最大次数](https://leetcode.cn/problems/maximum-number-of-moves-in-a-grid/description/)

[TOC]

# 思路

> 从第一列开始多源BFS，看能走到的最深层数
> 或者从第一列开始DFS，看能走到的最深层数

# 解题方法

> 答案最大为列数

# 复杂度

时间复杂度:
> $O(mn)$

空间复杂度:
> $O(m)$



# Code
```Python3 []
class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        ans, col, m, n = 0, 0, len(grid), len(grid[0])
        pq = deque([i for i in range(m)])
        while pq and col < n - 1:
            length = len(pq)
            explored = set()
            for _ in range(length):
                row = pq.popleft()
                for next_row in range(max(0, row - 1), min(m - 1, row + 1) + 1):
                    if grid[next_row][col + 1] > grid[row][col] and next_row not in explored:
                        pq.append(next_row)
                        explored.add(next_row)
            if len(explored):
                ans += 1
            col += 1
        return ans
```
```Python3 []
class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        @lru_cache(None)
        def dfs(i, j):
            if j == n - 1:
                return 0
            res = 0
            for ni in range(max(0, i - 1), min(m - 1, i + 1) + 1):
                if grid[ni][j + 1] > grid[i][j]:
                    res = max(res, dfs(ni, j + 1) + 1)
            return res
        
        return max(dfs(i, 0) for i in range(m))
```
  
