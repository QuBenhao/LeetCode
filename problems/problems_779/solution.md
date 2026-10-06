# [Python/Java/TypeScript/Go] Memoized recursion

> Author: Benhao
> Date: 2022-10-20
> Upvotes: 12
> Tags: Go, Java, JavaScript, Python, Python3, TypeScript

---

### Approach
The kth position in the current row comes from position `(k - 1) / 2 + 1` in the previous row

### Code

```python3 []
class Solution:
    @lru_cache(None)
    def kthGrammar(self, n: int, k: int) -> int:
        return 0 if n == 1 else int(not k % 2 if not self.kthGrammar(n - 1, (k - 1) // 2 + 1) else k % 2)
```
