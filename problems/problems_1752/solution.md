# [Python] 模拟

> Author: Benhao
> Date: 2022-11-27
> Upvotes: 4
> Tags: Go, Java, JavaScript, Python3, TypeScript

---

> Problem: [1752. 检查数组是否经排序和轮转得到](https://leetcode.cn/problems/check-if-array-is-sorted-and-rotated/description/)

[TOC]

# 思路
> 统计拐点个数

# 解题方法
> 只能有一个拐点

# 复杂度
- 时间复杂度: 
> $O(n)$

- 空间复杂度: 
> $O(n)$

# Code
```Python3 []

class Solution:
    def check(self, nums: List[int]) -> bool:
        return sum(a > b for a, b in pairwise([nums[-1]] + nums)) <= 1
```
