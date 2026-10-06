# [Python] Binary search

> slug: python-er-fen-by-himymben-e54f
> date: 2024-03-11
> tags: C, Go, Java, Python3, TypeScript
> question: Find Peak Element (find-peak-element)
> url: https://leetcode.cn/problems/find-peak-element/solutions/Vi0Wmk/python-er-fen-by-himymben-e54f/

---

> Problem: [162. 寻找峰值](https://leetcode.cn/problems/find-peak-element/description/)

[TOC]

# Intuition

> The problem asks for a turning point, where the direction of monotonicity changes. Use binary search based on that direction.

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
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < nums[mid + 1]:
                left = mid + 1
            else:
                right = mid
        return left
```
  
