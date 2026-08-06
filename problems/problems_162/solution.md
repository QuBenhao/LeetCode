# [Python] 二分

> slug: python-er-fen-by-himymben-e54f
> date: 2024-03-11
> tags: C, Go, Java, Python3, TypeScript
> question: Find Peak Element (find-peak-element)
> url: https://leetcode.cn/problems/find-peak-element/solutions/Vi0Wmk/python-er-fen-by-himymben-e54f/

---

> Problem: [162. 寻找峰值](https://leetcode.cn/problems/find-peak-element/description/)

[TOC]

# 思路

> 题目要求找拐点，实际上就是单调性发生变化的地方，我们按单调性二分即可

# 解题方法

> 二分

# 复杂度

时间复杂度:
> $O(log_n)$

空间复杂度:
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
  
