# [Python] 二分查找

> Author: Benhao
> Date: 2024-04-09
> Upvotes: 1
> Tags: C, Go, Java, Python3, TypeScript

---


> Problem: [2529. 正整数和负整数的最大计数](https://leetcode.cn/problems/maximum-count-of-positive-integer-and-negative-integer/description/)

[TOC]

# 思路

> 有序，找0的左右插入位置

# 解题方法

> 二分查找

# 复杂度

时间复杂度:
> $O(log_n)$

空间复杂度:
> $O(1)$


# Code
```Python3 []
class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        left, right = bisect_left(nums, 0), bisect_right(nums, 0)
        return max(0, left, len(nums) - right)
```
  
