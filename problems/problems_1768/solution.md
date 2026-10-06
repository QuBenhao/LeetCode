# [Python] Simulation

> Author: Benhao
> Date: 2022-10-23
> Upvotes: 6
> Tags: Go, Java, JavaScript, Python, Python3, TypeScript

---

### Approach
Simulate the process directly as described.

### Code

```python3
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        return "".join(f"{a}{b}" for a, b in zip_longest(word1, word2, fillvalue=""))
```
