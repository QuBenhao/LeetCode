# Simple simulation

> Author: Benhao
> Date: 2022-12-08
> Upvotes: 2
> Tags: Go, Java, JavaScript, Python3, TypeScript

---

> Problem: [1812. 判断国际象棋棋盘中一个格子的颜色](https://leetcode.cn/problems/determine-color-of-a-chessboard-square/description/)

[TOC]

# Intuition
> Simulate as described.

# Approach
> Check the parity of the horizontal and vertical coordinates.

# Complexity
- Time complexity:
> $O(1)$

- Space complexity:
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
