# Two-pointer simulation

> Author: Benhao
> Date: 2022-12-17
> Upvotes: 7
> Tags: Go, Java, JavaScript, Python3, TypeScript

---

> Problem: [1764. 通过连接另一个数组的子数组得到一个数组](https://leetcode.cn/problems/form-array-by-concatenating-subarrays-of-another-array/description/)

[TOC]

# Intuition
> Process each group in order and accept the first contiguous matching segment in nums.

# Approach
> Use two pointers and Python slices.

# Code
```Python3 []

class Solution:
    def canChoose(self, groups: List[List[int]], nums: List[int]) -> bool:
        i = idx = 0
        while i < len(groups) and idx < len(nums):
            if nums[idx:idx + len(groups[i])] == groups[i]:
                idx += len(groups[i])
                i += 1
            else:
                idx += 1
        return i == len(groups)

```
