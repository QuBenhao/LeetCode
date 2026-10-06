# [Python] Proof that even and odd powers of 2 have different remainders modulo 3

> Author: Benhao
> Date: 2021-05-31
> Upvotes: 4
> Tags: Python, Python3

---

### Approach
See the code comments for the proof.

My thoughts:

The modulus does not have to be 3, but 3 gives the shortest and fastest implementation.

For example, odd powers of `2` modulo 5 are **always 2 or 3**, while powers of `4` modulo 5 are **always 1 or 4**.
The following code can also distinguish odd and even powers of 2.
```python3
    return n & (n-1) == 0 and (n % 5 == 1 or n % 5 == 4) if n > 0 else False
```

### Code

```python3
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        # a % c = x, b % c = y --> ab % c = xy % c
        """
        Proof: Let a = m * c + x, b = n * c + y.
            a * b = m * n * c * c + x * n * c + y * m * c + x * y
            Therefore, a * b % c = x * y % c.
        """
        # The conclusion above gives two properties
        # Powers of 4 have remainder 1 modulo 3 (each factor 4 has remainder 1, so their product does too) 
        # An odd power of 2 is a power of 4 times 2, so its remainder modulo 3 is 1 times 2, or 2
        # Thus, odd and even powers of 2 have different remainders modulo 3
        return n & (n-1) == 0 and n % 3 == 1 if n > 0 else False
```
