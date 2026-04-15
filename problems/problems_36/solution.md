# [Python] 矩阵模拟

> Author: Benhao
> Date: 2024-03-01
> Upvotes: 7
> Tags: C, Go, Java, Python3

---


> Problem: [36. 有效的数独](https://leetcode.cn/problems/valid-sudoku/description/)

[TOC]

# 思路

> 依次遍历每行、每列、每个九宫格，判断是否有重复数字

# 解题方法

> 模拟

# 复杂度

时间复杂度:
> $O(n)$

空间复杂度:
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
  
