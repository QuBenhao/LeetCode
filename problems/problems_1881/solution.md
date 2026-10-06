# [Python] Greedy

> Author: Benhao
> Date: 2021-05-30
> Upvotes: 1
> Tags: Python, Python3

---

### Approach
The digit x must be inserted somewhere in the string.
For a negative number, insert x before the first digit greater than x; this gives a larger result than inserting it anywhere later.
For a positive number, insert x before the first digit smaller than x; this gives a larger result than inserting it anywhere later.

### Code

```python3
class Solution:
    def maxValue(self, n: str, x: int) -> str:
        if n[0]=='-':
            for i,c in enumerate(n[1:], 1):
                if int(c) > x:
                    return n[:i] + str(x) + n[i:]
            return n + str(x)
        else:
            for i,c in enumerate(n):
                if int(c) < x:
                    return n[:i] + str(x) + n[i:]
            return n + str(x)
```
