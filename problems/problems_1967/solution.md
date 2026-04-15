# [Python] 模拟

> Author: Benhao
> Date: 2021-08-15
> Upvotes: 1
> Tags: Python, Python3

---

```python3
class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        return sum(p in word for p in patterns)
```