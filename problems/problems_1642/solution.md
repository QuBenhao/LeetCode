# [Python] Max-heap

> Author: Benhao
> Date: 2021-05-31
> Upvotes: 1
> Tags: Python, Python3

---

### Approach
This resembles the problem about fighting monsters each round: spend bricks first and track the total needed. If bricks run out, reclaim the largest previous brick expenditure by using a ladder for that climb instead.

### Code

```python3
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        pq = []
        n = len(heights)
        for i in range(n-1):
            if heights[i+1] <= heights[i]:
                continue
            diff = heights[i+1] - heights[i]
            heapq.heappush(pq, -diff)
            bricks -= diff
            if bricks < 0 and ladders:
                ladders -= 1
                bricks -= heapq.heappop(pq)
            elif bricks < 0:
                return i
        return n - 1

```
