# [Python] 用2、3、5反复分解

> Author: Benhao
> Date: 2021-04-09
> Upvotes: 1
> Tags: Python

---

### 解题思路
除2、除3、除5，如果剩下的东西不是1，说明有其他质因数

### 代码

```python3
class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        while n % 2 == 0:
            n /= 2
        while n % 3 == 0:
            n /= 3
        while n % 5 == 0:
            n /= 5
        return n == 1

```