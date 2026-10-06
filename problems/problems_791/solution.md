# [Python] Sort by weights from order

> Author: Benhao
> Date: 2022-11-13
> Upvotes: 13
> Tags: Go, Java, JavaScript, Python3, TypeScript

---

> Problem: [791. 自定义字符串排序](https://leetcode.cn/problems/custom-sort-string/description/)

[TOC]

# Intuition
> To sort by order, assign each character a weight equal to its index in order, so smaller indices come first

# Approach
> Convert order to a hash map

# Complexity
- Time complexity: 
> $O(nlog_n)$

- Space complexity: 
> $O(n)$

# Code
```Python3 []

class Solution:
    def customSortString(self, order: str, s: str) -> str:
        return "".join(sorted(s, key=lambda x:mp.get(x, -1))) if (mp := {c: i for i, c in enumerate(order)}) else s
```
