# [Python] 模拟

> Author: Benhao
> Date: 2021-07-24
> Upvotes: 3
> Tags: Python, Python3

---

```python3
class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        return len(set(Counter(s).values())) == 1
```