# [Python] DP

> Author: Benhao
> Date: 2024-03-14
> Upvotes: 1
> Tags: C, Go, Java, Python3, TypeScript

---


> Problem: [64. 最小路径和](https://leetcode.cn/problems/minimum-path-sum/description/)

[TOC]

# Intuition

> Since we seek the minimum path sum and can move only right or down, the minimum for any cell comes from the smaller of the minimum sums to its left and upper neighbors. Maintain this minimum row by row.

# Approach

> Dynamic programming

# Complexity

Time complexity:
> $O(mn)$

Space complexity:
> $O(min(m, n))$



# Code
Row-by-row approach
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
Column-by-column approach
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
  
