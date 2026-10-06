# [Python] Binary search

> Author: Benhao
> Date: 2024-03-26
> Upvotes: 1
> Tags: C, Go, Java, Python3, TypeScript

---


> Problem: [33. 搜索旋转排序数组](https://leetcode.cn/problems/search-in-rotated-sorted-array/description/)

[TOC]

# Intuition

> First use binary search to find the rotation point. The section starting or ending at that point is increasing, so use binary search again to find target.

# Approach

> When binary-searching for the start at the rotation point, move the left pointer to the right when the value equals nums[0].

# Complexity

Time complexity:
> $O(log_n)$

Space complexity:
> $O(1)$



# Code
```Python3 []
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        idx = bisect_left(nums, True, key=lambda x: x < nums[0])
        ans = bisect_left(range(idx, n + idx - 1), True, key=lambda x: nums[x % n] >= target)
        return (idx + ans) % n if nums[(idx + ans) % n] == target else -1
```
```Python3 []
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        idx = bisect_left(nums, True, key=lambda x: x < nums[0])
        left, right = idx, n + idx - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid % n] < target:
                left = mid + 1
            else:
                right = mid
        return left % n if nums[left % n] == target else -1
```
```Python3 []
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = bisect_left(nums, True, key=lambda x:x<nums[0])
        if target >= nums[0]:
            idx = bisect_left(nums[:left], target)
            if idx < left:
                return idx if nums[idx] == target else -1
        else:
            idx = bisect_left(nums[left:], target)
            if idx < len(nums) - left:
                return ans if nums[(ans:=left + idx)] == target else -1
        return -1
```
```Python3 []
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target == nums[0]:
            return 0
        left, right = 0, len(nums)
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < nums[0]:
                right = mid
            else:
                left = mid + 1

        idx = left
        if target > nums[0]:
            left, right = 0, idx
        else:
            left, right = idx, len(nums)
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left if 0 <= left < len(nums) and nums[left] == target else -1
```
  
