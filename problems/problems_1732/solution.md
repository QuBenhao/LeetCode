# [Python] Simulation

> Author: Benhao
> Date: 2022-11-19
> Upvotes: 3
> Tags: Go, Java, JavaScript, Python3, TypeScript

---

> Problem: [1732. 找到最高海拔](https://leetcode.cn/problems/find-the-highest-altitude/description/)

[TOC]

# Intuition
> The input gives changes in altitude, so maintain a running sum.

# Approach
> Maximum prefix sum

# Complexity
- Time complexity:
> $O(n)$

- Space complexity:
> $O(n)$

# Code
```Python3 []

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        return max(0, max(accumulate(gain)))
```
