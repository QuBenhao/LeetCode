# [Python] Counter

> Author: Benhao
> Date: 2021-06-13
> Upvotes: 1
> Tags: Python, Python3

---

### Approach
Redistribution is possible only if every character's count can be divided evenly.

### Code

```python3
class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        counter = Counter()
        for w in words:
            for c in w:
                counter[c] += 1
        return all(v % len(words) == 0 for v in counter.values())

```
