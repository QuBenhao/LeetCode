# [Python] Backtracking

> Author: Benhao
> Date: 2024-03-11
> Upvotes: 1
> Tags: C, Go, Java, Python3, TypeScript

---


> Problem: [52. N 皇后 II](https://leetcode.cn/problems/n-queens-ii/description/)

[TOC]

# Intuition

> Fill each row in turn. If a row has no valid placement, backtrack and try another placement in an earlier row.

# Approach

> Use the sum and difference of the coordinates to check diagonal constraints quickly.

# Code
```Python3 []
class Solution:
    def totalNQueens(self, n: int) -> int:     
        self.ans = 0   
        cur = []
        # forward_set: /
        # back_set: \
        column_set, forward_set, back_set = set(), set(), set()
        def dfs(row):
            if row == n:
                self.ans += 1
                return
            for col in range(n):
                if col not in column_set and row + col not in forward_set and row - col not in back_set:
                    cur.append((row, col))
                    column_set.add(col)
                    forward_set.add(row+col)
                    back_set.add(row - col)
                    dfs(row + 1)
                    r, c = cur.pop()
                    column_set.remove(c)
                    forward_set.remove(r+c)
                    back_set.remove(r-c)
        
        dfs(0)
        return self.ans
```
  
