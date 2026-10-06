# [Python] Simulation

> Author: Benhao
> Date: 2022-11-27
> Upvotes: 4
> Tags: Go, Java, JavaScript, Python3, TypeScript

---

> Problem: [1752. 检查数组是否经排序和轮转得到](https://leetcode.cn/problems/check-if-array-is-sorted-and-rotated/description/)

[TOC]

# Intuition
> Count the drops between adjacent elements.

# Approach
> At most one drop is allowed.

# Complexity
- Time complexity:
> $O(n)$

- Space complexity:
> $O(n)$

# Code
```Python3 []

class Solution:
    def check(self, nums: List[int]) -> bool:
        return sum(a > b for a, b in pairwise([nums[-1]] + nums)) <= 1
```
