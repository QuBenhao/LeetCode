# [Python] DP

> Author: Benhao
> Date: 2024-03-13
> Upvotes: 1
> Tags: C, Go, Java, Python3, TypeScript

---


> Problem: [198. 打家劫舍](https://leetcode.cn/problems/house-robber/description/)

[TOC]

# 思路

> 当前的最大值由上一次没抢+这一次抢了，和上一次的最大值、这一次没抢组成

# 解题方法

> 动态规划

# 复杂度

时间复杂度:
> $O(n)$

空间复杂度:
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
  
