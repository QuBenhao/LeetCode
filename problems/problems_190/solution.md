# [Python] Simulation

> Author: Benhao
> Date: 2024-03-12
> Upvotes: 1
> Tags: C, Go, Java, Python3, TypeScript

---


> Problem: [190. 颠倒二进制位](https://leetcode.cn/problems/reverse-bits/description/)

[TOC]

# Intuition

> Check whether each bit is 1

# Approach

> Read n from right to left and build the result from left to right: right-shift one and left-shift the other.

# Complexity

Time complexity:
> $O(log_n)$

Space complexity:
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
  
