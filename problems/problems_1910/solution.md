# [Python] Simulation

> Author: Benhao
> Date: 2021-06-27
> Upvotes: 3
> Tags: Python, Python3

---

### Approach
This feels easier to write than the previous problem.

### Code

```python3
class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        while part in s:
            idx = s.index(part)
            s = s[:idx] + s[idx+len(part):]
        return s

```
