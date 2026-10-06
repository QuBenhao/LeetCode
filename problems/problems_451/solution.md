# [Python] Sort a Counter

> Author: Benhao
> Date: 2021-07-03
> Upvotes: 12
> Tags: Python, Python3

---

### Approach
Sort by frequency in descending order, then generate the result.

### Code

```python3
class Solution:
    def frequencySort(self, s: str) -> str:
        c = Counter(s)
        return "".join(v for v in sorted(c.keys(), key=lambda x:-c[x]) for i in range(c[v]))
```
