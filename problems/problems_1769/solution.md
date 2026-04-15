# 光芒熄灭了，但我们仍在战斗

> Author: Benhao
> Date: 2022-12-02
> Upvotes: 43
> Tags: Go, Java, JavaScript, Python3, TypeScript

---

> Problem: [1769. 移动所有球到每个盒子所需的最小操作数](https://leetcode.cn/problems/minimum-number-of-operations-to-move-all-balls-to-each-box/description/)

[TOC]

# 思路
> 方法一: 需要知道所有球的坐标
> 方法二: 逐位统计距离，当前左右侧的距离和可以从左盒子左边和右盒子右边快速得到

# 解题方法
> 方法一: 暴力统计
> 方法二: 前缀和优化

# 复杂度
方法一: 
- 时间复杂度: 
> $O(m * n)$

- 空间复杂度: 
> $O(n)$

方法二:
- 时间复杂度: 
> $O(n)$

- 空间复杂度: 
> $O(n)$

# Code
```Python3

class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        return [sum(abs(j - i) for j in idxes) for i in range(len(boxes))] if (idxes := [i for i, c in enumerate(boxes) if c == '1']) else [0] * len(boxes)

```
```Python3
class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        left, right = [0] * n, [0] * n
        cur = 0
        for i, c in enumerate(boxes):
            left[i], cur = left[i - 1] + cur, cur + (c == '1')
        cur = int(boxes[-1] == '1')
        for i in range(n - 2, -1, -1):
            right[i], cur = right[i + 1] + cur, cur + (boxes[i] == '1')
        return [left[i] + right[i] for i in range(n)]  
```
