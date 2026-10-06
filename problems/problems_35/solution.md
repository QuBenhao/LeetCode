# [Python] Binary search

> Author: Benhao
> Date: 2024-03-03
> Upvotes: 1
> Tags: C, Go, Java, Python3, TypeScript

---


> Problem: [35. 搜索插入位置](https://leetcode.cn/problems/search-insert-position/description/)

[TOC]

# Intuition

> Binary search

# Approach

> Search to the left when the values are equal.

# Complexity

Time complexity:
> $O(log_n)$

Space complexity:
> $O(log_n)$



# Code
```Python3 []
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return bisect_left(nums, target)
```
```Python3 []
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)
        while left < right:
            mid = (left + right) // 2
            if nums[mid] >= target:
                right = mid
            else:
                left = mid + 1
        return left
```
  
