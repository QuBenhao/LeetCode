# [Python] 贪心

> Author: Benhao
> Date: 2024-03-23
> Upvotes: 0
> Tags: C, Go, Java, Python3, TypeScript

---


> Problem: [2549. 统计桌面上的不同数字](https://leetcode.cn/problems/count-distinct-numbers-on-board/description/)

[TOC]

# 思路

> 对于每个数x,必能添加x-1，最多n天除1以外所有小于n的数都能被添加，返回n-1即可

# 解题方法

> 贪心

# 复杂度

时间复杂度:
> $O(1)$

空间复杂度:
> $O(1)$



# Code
```Python3 []
class Solution:
    def distinctIntegers(self, n: int) -> int:
        return n - 1 if n > 1 else 1
```
  
