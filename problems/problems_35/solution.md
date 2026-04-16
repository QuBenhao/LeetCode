# [Python] Binary search

> Author: Benhao
> Date: 2024-03-03
> Upvotes: 1
> Tags: C, Go, Java, Python3, TypeScript

---


> Problem: [35. 搜索插入位置](https://leetcode.cn/problems/search-insert-position/description/)

[TOC]

# 思路

> 二分查找

# 解题方法

> 相同的时候往左边找

# 复杂度

时间复杂度:
> $O(log_n)$

空间复杂度:
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
  
