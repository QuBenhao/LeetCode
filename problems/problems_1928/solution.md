# [Python] Min-heap by cost (200ms)

> Author: Benhao
> Date: 2021-07-10
> Upvotes: 7
> Tags: Python, Python3

---

### Approach
Similar to the [electric-car problem from the autumn contest](https://leetcode.cn/problems/DFPeFJ/).
Explore by minimum cost. A more expensive path to the same city should still enter the heap if it leaves more time available.

### Code

```python3
class Solution:
    def minCost(self, maxTime: int, edges: List[List[int]], passingFees: List[int]) -> int:
        n = len(passingFees)
        connect = defaultdict(lambda:defaultdict(lambda:1001))
        for a,b,t in edges:
            connect[a][b] = min(connect[a][b], t)
            connect[b][a] = min(connect[b][a], t)
        # fee, time, pos
        q = [(passingFees[0], maxTime, 0)]
        explored = {0:maxTime}
        while q:
            f, t, pos = heapq.heappop(q)
            if pos == n - 1:
                return f
            for nxt,tm in connect[pos].items():
                if tm > t:
                    continue
                if nxt not in explored or t - tm > explored[nxt]:
                    explored[nxt] = t - tm
                    heapq.heappush(q, (f + passingFees[nxt], t - tm, nxt))
        return -1
```
