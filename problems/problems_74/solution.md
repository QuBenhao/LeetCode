# [Python] View the matrix as a search tree from the bottom-left or bottom-right corner

> Author: Benhao
> Date: 2024-03-11
> Upvotes: 2
> Tags: C, Go, Java, Python3, TypeScript

---


> Problem: [74. 搜索二维矩阵](https://leetcode.cn/problems/search-a-2d-matrix/description/)

[TOC]

# Intuition

> Moving one way decreases the value, while moving the other way increases it. Search for target.

# Approach

> Direct binary search is still the best choice.

# Complexity

Time complexity:
> $O(mn)$

Space complexity:
> $O(1)$

# Code

```Python3 []
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        i, j = 0, n - 1
        while i < m and j >= 0:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                j -= 1
            else:
                i += 1
        return False
```
Binary search
```Python3 []
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])

        left, right = 0, m - 1
        while left < right:
            mid = (left + right + 1) // 2
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] < target:
                left = mid
            else:
                right = mid - 1
        idx = bisect_left(matrix[left], target)
        return idx < n and matrix[left][idx] == target
```
  
