# [Python] 标准的二分查找

> Author: Benhao
> Date: 2021-06-13
> Upvotes: 10
> Tags: Python, Python3

---

### 解题思路
代码即思路

### 代码

```python3
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left, right = 1, n
        while left < right:
            mid = (left + right) // 2
            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1
        return left

```