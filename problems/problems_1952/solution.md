# [Python] 因子个数为3只有质数的平方数

> Author: Benhao
> Date: 2021-08-01
> Upvotes: 2
> Tags: Python, Python3

---

```python3
class Solution:
    def isThree(self, n: int) -> bool:
        def isPrime(x):
            for i in range(2, int(math.sqrt(x)) + 1):
                if x % i == 0:
                    return False
            return True if x > 1 else False

        p = int(math.sqrt(n))
        return p * p == n and isPrime(p)

```