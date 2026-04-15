# [Python] 整数拆成多个整数（可重复）和使他们的乘积最大

> Author: Benhao
> Date: 2021-03-28
> Upvotes: 1
> Tags: Python

---

### 解题思路
尽可能地拆出3，其次2，不要1，如果余1就分出一个3拆出4来，如果余2就多加一个2.

### 代码

```python
class Solution(object):
    def maxNiceDivisors(self, primeFactors):
        """
        :type primeFactors: int
        :rtype: int
        """
        def power(x, y, p):
            res = 1     # Initialize result

            x = x % p  #Update x if it is more than or 
                        # equal to p

            while (y > 0):
                # If y is odd, multiply x with result
                if (y & 1):
                    res = (res*x) % p 
                    y=y-1
                # y must be even now
                y = y>>1  # y = y/2
                x = (x*x) % p  
            return res

        if primeFactors <= 3:
            return primeFactors
        mod = 10**9 + 7
        
        if primeFactors % 3 == 0:
            return power(3,primeFactors//3,mod)
        elif primeFactors % 3 == 1:
            return (power(3, (primeFactors-4)//3, mod) * 4) %mod
        else:
            return (power(3, (primeFactors-2)//3, mod) * 2) %mod
```