# [Python] Group monsters by arrival time

> Author: Benhao
> Date: 2021-07-04
> Upvotes: 1
> Tags: Python, Python3

---

### Approach
Eliminate the earliest-arriving monsters first. Return when there is no longer enough time to eliminate them all.
Group by ceiling division minus 1, so each bucket covers (k-1, k].
By minute k, every monster in that interval has arrived.

### Code

```python3
class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        cnts = Counter()
        for d,s in zip(dist,speed):
            cnts[ceil(d/s)-1] += 1
        ans = 0
        for k in sorted(cnts.keys()):
            if cnts[k] > k + 1 - ans:
                return k + 1
            ans += cnts[k]
        return ans
```
