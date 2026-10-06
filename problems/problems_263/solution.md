# [Python] Repeatedly factor out 2, 3, and 5

> Author: Benhao
> Date: 2021-04-09
> Upvotes: 1
> Tags: Python

---

### Approach
Divide by 2, 3, and 5. If the remainder is not 1, another prime factor exists.

### Code

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
