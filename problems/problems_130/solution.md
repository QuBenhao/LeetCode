# [Python] DFS

> slug: python-dfs-by-himymben-72gp
> date: 2024-03-09
> tags: C, Go, Java, Python3, TypeScript
> question: Surrounded Regions (surrounded-regions)
> url: https://leetcode.cn/problems/surrounded-regions/solutions/XmIHLp/python-dfs-by-himymben-72gp/

---

> Problem: [130. 被围绕的区域](https://leetcode.cn/problems/surrounded-regions/description/)

[TOC]

# 思路

> 找中间的联通部分不如从两边找不用变X的所有O，那么剩下的所有O都是要变X的

# 解题方法

> DFS

# 复杂度

时间复杂度:
> $O(mn)$

空间复杂度:
> $O(mn)$



# Code
边缘优化
```Python3 []
DIRS = [(0, 1), (1, 0), (-1, 0), (0, -1)]
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        def dfs(x, y):
            if x < 0 or x == m or y == n or y < 0 or board[x][y] != 'O':
                return
            board[x][y] = ''
            for dx, dy in DIRS:
                dfs(x + dx, y + dy)
        
        for j in range(n):
            dfs(0, j)
            dfs(m - 1, j)
        for i in range(m):
            dfs(i, 0)
            dfs(i, n - 1)
        for i in range(m):
            for j in range(n):
                if board[i][j] == '':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'
```
普通遍历
```python3 []
DIRS = [(0, 1), (1, 0), (-1, 0), (0, -1)]
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        def dfs(x, y):
            explored.add((x, y))
            for dx, dy in DIRS:
                if (nx:=x+dx) < 0 or nx == m or (ny:=y+dy) < 0 or ny == n:
                    return False
                elif board[nx][ny] == 'O' and (nx, ny) not in explored:
                    if not dfs(nx, ny):
                        return False
            return True
        
        def draw(x, y):
            board[x][y] = 'X'
            for dx, dy in DIRS:
                if (nx:=x+dx) < 0 or nx == m or (ny:=y+dy) < 0 or ny == n or board[nx][ny] == 'X':
                    return
                else:
                    draw(nx, ny)
        
        for i in range(m):
            for j in range(n):
                explored = set()
                if board[i][j] == 'O' and dfs(i, j):
                    draw(i, j)
```

  
