# [Python] Dynamic programming with rolling updates

> Author: Benhao
> Date: 2024-03-25
> Upvotes: 2
> Tags: C, Go, Java, Python3, TypeScript

---


> Problem: [63. 不同路径 II](https://leetcode.cn/problems/unique-paths-ii/description/)

[TOC]

# Intuition

> The number of paths to (i, j) comes from the path counts at (i - 1, j) and (i, j - 1). Maintain the path count and reset it to zero at obstacles.

# Approach

> Dynamic programming with rolling updates

# Complexity

Time complexity:
> $O(mn)$

Space complexity:
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
  
