# [Python] 动态规划滚动更新

> Author: Benhao
> Date: 2024-03-25
> Upvotes: 2
> Tags: C, Go, Java, Python3, TypeScript

---


> Problem: [63. 不同路径 II](https://leetcode.cn/problems/unique-paths-ii/description/)

[TOC]

# 思路

> (i, j)点的路线数由(i - 1, j)点的路线数和(i, j - 1)点的路线数构成，我们维护一个路线数，在遇到障碍时清零即可。

# 解题方法

> 动态规划滚动更新

# 复杂度

时间复杂度:
> $O(mn)$

空间复杂度:
> $O(n)$



# Code
```Python3 []
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [0] * n
        dp[0] = 1
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    dp[j] = 0
                elif j > 0:
                    dp[j] += dp[j - 1]
        return dp[-1]
```
  
