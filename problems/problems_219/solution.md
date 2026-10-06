# [Python] Sliding window

> Author: Benhao
> Date: 2024-04-11
> Upvotes: 1
> Tags: C, Go, Java, Python3, TypeScript

---


> Problem: [219. 存在重复元素 II](https://leetcode.cn/problems/contains-duplicate-ii/description/)

[TOC]

# Intuition

> Maintain a set of k values in a sliding window and check for duplicates.

# Approach

> Sliding window

# Complexity

Time complexity:
> $O(n)$

Space complexity:
> $O(k)$



# Code
```Python3 []
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()
        for i, num in enumerate(nums):
            if num in window:
                return True
            window.add(num)
            if i >= k:
                window.remove(nums[i - k])
        return False
```
  
