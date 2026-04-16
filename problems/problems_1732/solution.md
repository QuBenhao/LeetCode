# [Python] 模拟

> Author: Benhao
> Date: 2022-11-19
> Upvotes: 3
> Tags: Go, Java, JavaScript, Python3, TypeScript

---

> Problem: [1732. 找到最高海拔](https://leetcode.cn/problems/find-the-highest-altitude/description/)

[TOC]

# 思路
> 题目给定的是变化量，我们维护一个和即可

# 解题方法
> 前缀和最大值

# 复杂度
- 时间复杂度: 
> $O(n)$

- 空间复杂度: 
> $O(n)$

# Code
```Python3 []

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        return max(0, max(accumulate(gain)))
```
