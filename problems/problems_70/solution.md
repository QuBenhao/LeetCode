# [Python] 动态规划

> Author: Benhao
> Date: 2024-03-04
> Upvotes: 1
> Tags: C, Go, Java, Python3, TypeScript

---


> Problem: [70. 爬楼梯](https://leetcode.cn/problems/climbing-stairs/description/)

[TOC]

# 思路

> 动态规划滚动更新

# 解题方法

> 当前的组合数由上一层走一步+上两层走两步组成

# 复杂度

时间复杂度:
> $O(n)$

空间复杂度:
> $O(1)$



# Code
```Python3 []
class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0] * 3
        dp[0] = 1
        for i in range(1, n + 1):
            dp[i % 3] = dp[(i - 1) % 3] + dp[(i - 2) % 3]
        return dp[n % 3]
```
  
