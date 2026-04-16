# [Python] 费用最小堆 (200ms)

> Author: Benhao
> Date: 2021-07-10
> Upvotes: 7
> Tags: Python, Python3

---

### 解题思路
有点儿像[秋季赛的电动车](https://leetcode.cn/problems/DFPeFJ/)
考虑遍历最小费用，如果同一个城市出现更多费用，但是可以获得更多时间的时候，仍然加入堆

### 代码

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