# [Python] DP

> Author: Benhao
> Date: 2024-03-14
> Upvotes: 1
> Tags: C, Go, Java, Python3, TypeScript

---


> Problem: [64. 最小路径和](https://leetcode.cn/problems/minimum-path-sum/description/)

[TOC]

# 思路

> 找最小路径且只能往右或往下，那么任意格子的最小路径由它左边和上边的最小路径中更小的一个构成。我们逐行维护这个最小值即可

# 解题方法

> 动态规划

# 复杂度

时间复杂度:
> $O(mn)$

空间复杂度:
> $O(min(m, n))$



# Code
逐行写法
```Python3 []
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [inf] * n
        dp[0] = 0
        for i in range(m):
            dp[0] += grid[i][0]
            for j in range(1, n):
                dp[j] = min(dp[j - 1] + grid[i][j], dp[j] + grid[i][j])
        return dp[-1]
```
逐列写法
```Python3 []
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [inf] * m
        dp[0] = 0
        for i in range(n):
            dp[0] += grid[0][i]
            for j in range(1, m):
                dp[j] = min(dp[j - 1] + grid[j][i], dp[j] + grid[j][i])
        return dp[-1]
```
  
