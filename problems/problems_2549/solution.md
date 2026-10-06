# [Python] Greedy

> Author: Benhao
> Date: 2024-03-23
> Upvotes: 0
> Tags: C, Go, Java, Python3, TypeScript

---


> Problem: [2549. 统计桌面上的不同数字](https://leetcode.cn/problems/count-distinct-numbers-on-board/description/)

[TOC]

# Intuition

> For each number x, x-1 can be added. Within at most n days, every number smaller than n except 1 can be added; return n-1.

# Approach

> Greedy

# Complexity

Time complexity:
> $O(1)$

Space complexity:
> $O(1)$



# Code
```Python3 []
class Solution:
    def distinctIntegers(self, n: int) -> int:
        return n - 1 if n > 1 else 1
```
  
