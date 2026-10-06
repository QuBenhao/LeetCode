# [Python] Bit manipulation 100%

> Author: Benhao
> Date: 2021-05-29
> Upvotes: 5
> Tags: Python, Python3

---

### Approach
Use `x&(-x)==x` or `x&(x-1)==0` to check for a power of 2.
> x&(-x) isolates the rightmost set bit of x. If n equals that value, n has only this one set bit and must therefore be a power of 2.
> Likewise, subtracting one from a power of 2 produces the opposite bit pattern across its binary digits. A bitwise AND of 0 indicates a power of 2.

### Code

```python3
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n == n & (-n) if n else False
```

```python3
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return not n & (n-1) if n else False
```
