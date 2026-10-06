# [Python] Greedy

> Author: Benhao
> Date: 2021-07-18
> Upvotes: 1
> Tags: Python, Python3

---

### Approach
Climb whenever the next rung is reachable; otherwise, add enough rungs to reach it.

### Code

```python3
class Solution:
    def addRungs(self, rungs: List[int], dist: int) -> int:
        cur = ans = 0
        for h in rungs:
            ans += (h - cur - 1) // dist
            cur = h
        return ans
```
