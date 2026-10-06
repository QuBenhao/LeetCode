# [Python] Fast matrix exponentiation

> Author: Benhao
> Date: 2024-03-22
> Upvotes: 1
> Tags: C, Go, Java, Python3, TypeScript

---


> Problem: [50. Pow(x, n)](https://leetcode.cn/problems/powx-n/description/)

[TOC]

# Intuition

> Fast matrix exponentiation

# Approach

> Mathematically, $x^a = x^b * x^c$, where $a=b+c$.
> View n as the sum of the place values of its binary digits, for example $(1001)_b$.
> We know that $x^8=x^4*x^4$, $x^4=x^2*x^2$, and $x^2=x*x$.
> Work from right to left, repeatedly squaring the current value and including it in the answer only when the binary digit is 1.

# Complexity

Time complexity:
> $O(log_2n)$

Space complexity:
> $O(1)$



# Code
```Python3 []
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0.0:
            return 0.0
        if n < 0:
            x, n = 1 / x, -n
        ans = 1.0
        while n:
            if n & 1:
                ans *= x
            x *= x
            n >>= 1
        return ans
```
  
