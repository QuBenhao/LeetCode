# 简单模拟题

> Author: Benhao
> Date: 2022-12-08
> Upvotes: 2
> Tags: Go, Java, JavaScript, Python3, TypeScript

---

> Problem: [1812. 判断国际象棋棋盘中一个格子的颜色](https://leetcode.cn/problems/determine-color-of-a-chessboard-square/description/)

[TOC]

# 思路
> 按题意模拟

# 解题方法
> 根据横纵坐标奇偶性判断即可

# 复杂度
- 时间复杂度: 
> $O(1)$

- 空间复杂度: 
> $O(1)$

# Code
```Python3 []

class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        return (ord(coordinates[0]) - ord('a') & 1) != (ord(coordinates[1]) - ord('1') & 1)
```
```Go []
func squareIsWhite(coordinates string) bool {
    return (coordinates[0] - 'a') & 1 != (coordinates[1] - '1') & 1
}
```
