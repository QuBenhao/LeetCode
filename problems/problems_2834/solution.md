# [Python] 数学

> slug: python-shu-xue-by-himymben-8zmh
> date: 2024-03-08
> tags: C, Go, Java, Python3, TypeScript
> question: Find the Minimum Possible Sum of a Beautiful Array (find-the-minimum-possible-sum-of-a-beautiful-array)
> url: https://leetcode.cn/problems/find-the-minimum-possible-sum-of-a-beautiful-array/solutions/VkdDge/python-shu-xue-by-himymben-8zmh/

---

> Problem: [2834. 找出美丽数组的最小和](https://leetcode.cn/problems/find-the-minimum-possible-sum-of-a-beautiful-array/description/)

[TOC]

# 思路

> 本题取法是唯一的，从1取到target的一半(下取整)，再从target开始取直到取够n个

# 解题方法

> 用两次求和公式即可

# 复杂度

时间复杂度:
> $O(1)$

空间复杂度:
> $O(1)$



# Code
```Python3 []
MOD = int(1e9) + 7
class Solution:
    def minimumPossibleSum(self, n: int, target: int) -> int:
        return ((1 + m) * m // 2 + (target + target + n - m - 1) * (n - m) // 2) % MOD if (m := min(n, target // 2)) >= 0 else 0
```
  
