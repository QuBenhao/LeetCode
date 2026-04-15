# [Python] 从左下角或者右下角看的搜索树

> Author: Benhao
> Date: 2024-03-11
> Upvotes: 2
> Tags: C, Go, Java, Python3, TypeScript

---


> Problem: [74. 搜索二维矩阵](https://leetcode.cn/problems/search-a-2d-matrix/description/)

[TOC]

# 思路

> 往一边会变小，往另一边会变大，找能不能遇到target

# 解题方法

> 当然最好还是二分直接找

# 复杂度

时间复杂度:
> $O(mn)$

空间复杂度:
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
二分查找
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
  
