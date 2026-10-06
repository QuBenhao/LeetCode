# [Python] Binary search

> Author: Benhao
> Date: 2021-05-23
> Upvotes: 3
> Tags: Python, Python3

---

### Approach
Departures must be on whole hours, but the final arrival need not be, so do not round up the last segment.

### Code

```python3
class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        def helper(v):
            h = 0.0
            for d in dist[:-1]:
                t = float(d)/v
                h += ceil(t)
            h += float(dist[-1])/v
            return h <= hour
        
        if hour <= len(dist) - 1:
            return -1
        l,r = 1, 10 ** 7
        while l < r:
            mid = (l+r)//2
            if helper(mid):
                r = mid
            else:
                l = mid + 1
        return l
```
