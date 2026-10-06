# [Python] Matrix simulation

> Author: Benhao
> Date: 2024-03-01
> Upvotes: 7
> Tags: C, Go, Java, Python3

---


> Problem: [36. 有效的数独](https://leetcode.cn/problems/valid-sudoku/description/)

[TOC]

# Intuition

> Traverse each row, column, and 3x3 box, checking for duplicate digits.

# Approach

> Simulation

# Complexity

Time complexity:
> $O(n)$

Space complexity:
> $O(n)$



# Code
```Python3 []
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            sr, sc, ss = set(), set(), set()
            for j in range(9):
                if board[i][j] != ".":
                    if board[i][j] in sr:
                        return False
                    sr.add(board[i][j])
                if board[j][i] != ".":
                    if board[j][i] in sc:
                        return False
                    sc.add(board[j][i])
                row, col = i // 3 * 3 + j // 3, i % 3 * 3 + j % 3
                if board[row][col] != ".":
                    if board[row][col] in ss:
                        return False
                    ss.add(board[row][col])
        return True
```
  
