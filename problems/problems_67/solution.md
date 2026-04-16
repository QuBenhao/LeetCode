# [Python] 模拟

> Author: Benhao
> Date: 2024-03-04
> Upvotes: 2
> Tags: C, Go, Java, Python3, TypeScript

---


> Problem: [67. 二进制求和](https://leetcode.cn/problems/add-binary/description/)

[TOC]

# 思路

> 从后往前遍历，维护进位

# 解题方法

> 模拟

# 复杂度

时间复杂度:
> $O(n)$

空间复杂度:
> $O(n)$



# Code
```Python3 []
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = []
        last = 0
        for char_a, char_b in zip_longest(a[::-1], b[::-1], fillvalue='0'):
            cur = (ord(char_a) - ord('0')) + (ord(char_b) - ord('0')) + last
            res.append('0' if cur % 2 == 0 else '1')
            last = 1 if cur >= 2 else 0
        if last:
            res.append('1')
        return ''.join(res[::-1])
```
  
