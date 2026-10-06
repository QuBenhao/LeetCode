# [Python] Sorted list

> Author: Benhao
> Date: 2021-06-22
> Upvotes: 3
> Tags: Python, Python3

---

### Approach
Simulate each insertion by counting the numbers on either side, using distances between indices in sorted order.
A sorted list supports o(logn) binary search and o(logn) insertion per number, for o(n * logn) overall.

### Code

```python3
from sortedcontainers import SortedList


class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        pq = SortedList([])
        ans = 0
        for i in instructions:
            ans = (ans + min(pq.bisect_left(i), len(pq) - pq.bisect_right(i))) % (10 ** 9 + 7)
            pq.add(i)
        return ans
```
