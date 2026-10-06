# [Python] Dynamic programming

> Author: Benhao
> Date: 2024-03-04
> Upvotes: 1
> Tags: C, Go, Java, Python3, TypeScript

---


> Problem: [70. 爬楼梯](https://leetcode.cn/problems/climbing-stairs/description/)

[TOC]

# Intuition

> Dynamic programming with rolling updates

# Approach

> The current count combines taking one step from the previous stair and two steps from the stair before that.

# Complexity

Time complexity:
> $O(n)$

Space complexity:
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
  
