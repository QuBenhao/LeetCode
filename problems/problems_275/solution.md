# [Python] Binary search

> Author: Benhao
> Date: 2021-07-11
> Upvotes: 2
> Tags: Python, Python3

---

### Approach
The same as yesterday, except the order is ascending, so use n-mid.

### Code

```python3
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        l, r = 0, n
        while l < r:
            mid = l + r + 1 >> 1
            if citations[n - mid] >= mid:
                l = mid
            else:
                r = mid - 1
        return l
```
