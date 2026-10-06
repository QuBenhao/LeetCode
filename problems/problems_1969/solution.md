# [Python] One-line greedy solution

> Author: Benhao
> Date: 2021-08-15
> Upvotes: 1
> Tags: Python, Python3

---

### Approach
No time for a proof; see 灵老师's explanation.

### Code

```python3
class Solution:
    def minNonZeroProduct(self, p: int) -> int:
        return (m:=(2 ** p - 1)) * pow(m - 1, m//2, 10 ** 9 + 7) % (10 ** 9 + 7)
```
