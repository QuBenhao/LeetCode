# [Python] Fermat's theorem on sums of two squares

> Author: Benhao
> Date: 2021-04-28
> Upvotes: 9
> Tags: Python, Python3

---

### Approach
By Fermat's theorem on sums of two squares, check that each prime factor congruent to 3 modulo 4 has an even exponent.

### Code

```python3
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        if not c:
            return True
        # (a - b) ^ 2 + (a + b) ^ 2 = 2 * (a ^ 2 + b ^ 2) = 2 * c
        while c % 2 == 0:
            c //= 2
        # Fermat's theorem on sums of two squares
        if c % 4 == 3:
            return False
        sqrt = int(math.sqrt(c))
        for i in range(3, sqrt + 1, 4):
            count = 0
            while c % i == 0:
                c //= i
                count += 1
            if count % 2 != 0:
                return False
        return True
```
