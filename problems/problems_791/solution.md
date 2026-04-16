# [Python] 按order权重排序

> Author: Benhao
> Date: 2022-11-13
> Upvotes: 13
> Tags: Go, Java, JavaScript, Python3, TypeScript

---

> Problem: [791. 自定义字符串排序](https://leetcode.cn/problems/custom-sort-string/description/)

[TOC]

# 思路
> 既然是按order排序，那么order会给每个字符一个权重，按坐标即可，这样坐标小的权重就靠前

# 解题方法
> 将order转化成哈希表

# 复杂度
- 时间复杂度: 
> $O(nlog_n)$

- 空间复杂度: 
> $O(n)$

# Code
```Python3 []

class Solution:
    def customSortString(self, order: str, s: str) -> str:
        return "".join(sorted(s, key=lambda x:mp.get(x, -1))) if (mp := {c: i for i, c in enumerate(order)}) else s
```
