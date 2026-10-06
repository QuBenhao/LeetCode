# [Python] Simulation

> Author: Benhao
> Date: 2022-11-01
> Upvotes: 6
> Tags: Go, Java, JavaScript, Python, Python3, TypeScript

---

### Approach
Use iterators to compare characters one by one.

### Code

```python3
class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        return all(a == b for a, b in zip_longest(chain.from_iterable(word1), chain.from_iterable(word2)))
```

```Python3
class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        return "".join(word1) == "".join(word2)
```
