# [Python] Fast exponentiation

> Author: Benhao
> Date: 2021-07-04
> Upvotes: 1
> Tags: Python, Python3

---

### Approach
Even indices have five choices, 0,2,4,6,8, including a leading 0; odd indices have four prime choices, 2,3,5,7.
Multiply the number of choices for the even positions by the number for the odd positions.

### Code

```python3
class Solution:
    def countGoodNumbers(self, n: int) -> int:
        # Even indices: 0, 2, 4, 6, 8; odd indices: 2, 3, 5, 7
        return (pow(5, ceil(n/2), 10**9+7) * pow(4, n//2, 10**9+7)) % (10**9+7)
```
