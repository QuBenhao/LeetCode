# [Python] Exhaustive search

> Author: Benhao
> Date: 2022-10-30
> Upvotes: 14
> Tags: Go, Java, JavaScript, Python, Python3, TypeScript

---

### Approach
Process each letter position according to the problem statement

### Code

```python3
class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        ans = [""]
        for i, c in enumerate(s):
            if c.isalpha():
                ans = [a + c.lower() for a in ans] + [a + c.upper() for a in ans]
            else:
                ans = [a + c for a in ans]
        return ans
```
