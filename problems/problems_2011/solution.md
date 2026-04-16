# [Python] 模拟

> Author: Benhao
> Date: 2022-12-23
> Upvotes: 7
> Tags: Go, Java, JavaScript, Python3, TypeScript

---

```Python3 []
class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        return sum(1 if "++" in op else -1 for op in operations)
```