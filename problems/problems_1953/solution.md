# [Python] Greedy

> Author: Benhao
> Date: 2021-08-01
> Upvotes: 1
> Tags: Python, Python3

---

### Approach
To maximize the number of weeks, schedule as much work as possible. Including every milestone of the largest project requires other projects between them, so we need at least maximum-1 other milestones. If the largest project fits, distribute the others among its gaps.

If the largest project cannot be separated this way, the sum of all other projects determines the limit.

### Code

```python3
class Solution:
    def numberOfWeeks(self, milestones: List[int]) -> int:
        m, s = max(milestones), sum(milestones)
        return (s - m) * 2 + 1 if m > s - m else s
```
