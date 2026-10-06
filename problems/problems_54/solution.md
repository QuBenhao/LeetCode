# [Python] Simulation

> Author: Benhao
> Date: 2024-03-06
> Upvotes: 1
> Tags: C, Go, Java, Python3, TypeScript

---


> Problem: [54. 螺旋矩阵](https://leetcode.cn/problems/spiral-matrix/description/)

[TOC]

# Intuition

> Turn when the next position is beyond the boundary or has already been visited.

# Approach

> Use a direction array to move the coordinates when turning.

# Complexity

Time complexity:
> $O(mn)$

Space complexity:
> $O(mn)$



# Code
```Python3 []
DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        m, n = len(matrix), len(matrix[0])
        i = j = d = 0
        for _ in range(m * n):
            ans.append(matrix[i][j])
            matrix[i][j] = inf
            if (nx := i + DIRS[d][0]) < 0 or nx == m or (ny := j + DIRS[d][1]) < 0 or ny == n or matrix[nx][ny] == inf:
                d = (d + 1) % len(DIRS)
                i, j = i + DIRS[d][0], j + DIRS[d][1]
            else:
                i, j = nx, ny
        return ans
```
  
