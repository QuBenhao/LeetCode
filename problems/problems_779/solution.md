# [Python/Java/TypeScript/Go] 记忆化递归

> Author: Benhao
> Date: 2022-10-20
> Upvotes: 12
> Tags: Go, Java, JavaScript, Python, Python3, TypeScript

---

### 解题思路
当前行的第k位由上一行的第`(k - 1) / 2 + 1`得到

### 代码

```python3 []
class Solution:
    @lru_cache(None)
    def kthGrammar(self, n: int, k: int) -> int:
        return 0 if n == 1 else int(not k % 2 if not self.kthGrammar(n - 1, (k - 1) // 2 + 1) else k % 2)
```