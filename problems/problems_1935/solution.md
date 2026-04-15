# [Python] 模拟

> Author: Benhao
> Date: 2021-07-18
> Upvotes: 1
> Tags: Python, Python3

---

```python3
class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        bk = set(brokenLetters)
        return sum(all(c not in bk for c in s) for s in text.split(' '))

```