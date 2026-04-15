# [Python] 模拟

> Author: Benhao
> Date: 2024-03-12
> Upvotes: 1
> Tags: C, Go, Java, Python3, TypeScript

---


> Problem: [190. 颠倒二进制位](https://leetcode.cn/problems/reverse-bits/description/)

[TOC]

# 思路

> 逐位判断是否为1

# 解题方法

> n从右往左看，结果从左往右看，只需要一个右移，一个左移

# 复杂度

时间复杂度:
> $O(log_n)$

空间复杂度:
> $O(1)$


# Code
```Python3 []
class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0
        for _ in range(32):
            ans = ans << 1 | (n & 1)
            n >>= 1
        return ans
```
  
