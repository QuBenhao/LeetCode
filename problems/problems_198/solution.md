# [Python] DP

> Author: Benhao
> Date: 2024-03-13
> Upvotes: 1
> Tags: C, Go, Java, Python3, TypeScript

---


> Problem: [198. 打家劫舍](https://leetcode.cn/problems/house-robber/description/)

[TOC]

# Intuition

> The current maximum is the greater of skipping the previous house and robbing this one, or keeping the previous maximum and skipping this house.

# Approach

> Dynamic programming

# Complexity

Time complexity:
> $O(n)$

Space complexity:
> $O(1)$



# Code
```Python3 []
class Solution:
    def rob(self, nums: List[int]) -> int:
        dp_rob, dp_not = 0, 0
        for num in nums:
            dp_rob, dp_not = dp_not + num, max(dp_rob, dp_not)
        return max(dp_rob, dp_not)
```
  
