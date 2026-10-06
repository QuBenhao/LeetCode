# [Python] Binary search

> Author: Benhao
> Date: 2024-04-09
> Upvotes: 1
> Tags: C, Go, Java, Python3, TypeScript

---


> Problem: [2529. 正整数和负整数的最大计数](https://leetcode.cn/problems/maximum-count-of-positive-integer-and-negative-integer/description/)

[TOC]

# Intuition

> The array is sorted; find the left and right insertion positions for 0.

# Approach

> Binary search

# Complexity

Time complexity:
> $O(log_n)$

Space complexity:
> $O(1)$


# Code
```Python3 []
class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        left, right = bisect_left(nums, 0), bisect_right(nums, 0)
        return max(0, left, len(nums) - right)
```
  
