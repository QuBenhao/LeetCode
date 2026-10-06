# [Python] Compute each value directly

> Author: Benhao
> Date: 2021-05-30
> Upvotes: 1
> Tags: Python, Python3

---

### Approach
See the code.

### Code

```python3
class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        def helper(s):
            res = 0
            for c in s:
                res = 10 * res + ord(c) - ord('a')
            return res

        return helper(firstWord) + helper(secondWord) == helper(targetWord)
```
