# [Python] XOR, then count the 1 bits

> Author: Benhao
> Date: 2021-05-27
> Upvotes: 1
> Tags: Python, Python3

---

### Approach
This user was too lazy to write more than one line of code.

### Code

```python3
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return bin(x ^ y).count('1')
```
