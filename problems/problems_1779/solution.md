# [Python] 模拟

> Author: Benhao
> Date: 2022-11-30
> Upvotes: 6
> Tags: Go, Java, JavaScript, Python3, TypeScript

---

> Problem: [1779. 找到最近的有相同 X 或 Y 坐标的点](https://leetcode.cn/problems/find-nearest-point-that-has-the-same-x-or-y-coordinate/description/)

[TOC]

# 思路
> 按题意模拟

# 解题方法
> 遍历

# 复杂度
- 时间复杂度: 
> $O(n)$

- 空间复杂度: 
> $O(1)$

# Code
```Python3 []

class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        idx, cur = -1, inf
        for i, (a, b) in enumerate(points):
            if (x == a or y == b) and (dis := abs(x - a) + abs(y - b)) < cur:
                idx, cur = i, dis
        return idx

```
