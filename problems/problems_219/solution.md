# [Python] 滑动窗口

> Author: Benhao
> Date: 2024-04-11
> Upvotes: 1
> Tags: C, Go, Java, Python3, TypeScript

---


> Problem: [219. 存在重复元素 II](https://leetcode.cn/problems/contains-duplicate-ii/description/)

[TOC]

# 思路

> 滑窗维护k个数的集合，判断有没有重复即可

# 解题方法

> 滑动窗口

# 复杂度

时间复杂度:
> $O(n)$

空间复杂度:
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
  
