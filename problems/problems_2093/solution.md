# [Python] Track the minimum cost for each position and remaining discount count

> slug: python-by-himymben-sx05
> date: 2022-05-02
> tags: Python, Python3
> question: Minimum Cost to Reach City With Discounts (minimum-cost-to-reach-city-with-discounts)
> url: https://leetcode.cn/problems/minimum-cost-to-reach-city-with-discounts/solutions/t8LuET/python-by-himymben-sx05/

---
### Approach
If a smaller cost is found for the same position and remaining discount count, enqueue the state again.

### Code

```python3
class Solution:
    def minimumCost(self, n: int, highways: List[List[int]], discounts: int) -> int:
        graph = defaultdict(lambda:defaultdict(int))
        for a, b, c in highways:
            graph[a][b] = c
            graph[b][a] = c
        explored = defaultdict(lambda:defaultdict(int))
        explored[0][discounts] = 0
        queue = deque([(0, discounts)])
        ans = defaultdict(lambda:defaultdict(lambda:inf))
        ans[0][discounts] = 0
        while queue:
            idx, ds = queue.popleft()
            for other, v in graph[idx].items():
                if ds:
                    if ans[other][ds - 1] > ans[idx][ds] + v // 2:
                        ans[other][ds - 1] = ans[idx][ds] + v // 2
                        queue.append((other, ds - 1))
                if ans[other][ds] > ans[idx][ds] + v:
                    ans[other][ds] = ans[idx][ds] + v
                    queue.append((other, ds))
        return m if ans[n-1] and (m:= min(ans[n - 1].values())) != inf else -1

```
