# [Python] 矩阵快速幂

> Author: Benhao
> Date: 2024-03-22
> Upvotes: 1
> Tags: C, Go, Java, Python3, TypeScript

---


> Problem: [50. Pow(x, n)](https://leetcode.cn/problems/powx-n/description/)

[TOC]

# 思路

> 矩阵快速幂

# 解题方法

> 数学里面有$x^a = x^b * x^c$,其中$a=b+c$
> 那么我们可以将n看成是它的二进制各数位的和，比如$(1001)_b$
> 我们知道$x^8=x^4*x^4$，而$x^4=x^2*x^2$，$x^2=x*x$
> 我们从右到左不停连乘自己，仅在二进制位数是1时计入答案，就可以得到结果

# 复杂度

时间复杂度:
> $O(log_2n)$

空间复杂度:
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
  
