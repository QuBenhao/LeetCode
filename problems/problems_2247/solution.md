# [Python] Bitmask states + memoized recursion

> slug: python-by-himymben-umzg
> date: 2022-04-23
> tags: Python, Python3
> question: Maximum Cost of Trip With K Highways (maximum-cost-of-trip-with-k-highways)
> url: https://leetcode.cn/problems/maximum-cost-of-trip-with-k-highways/solutions/IVYXCK/python-by-himymben-umzg/

---
### Approach
Use a bitmask to mark visited nodes.

### Code

```python3
class Solution:
    def maximumCost(self, n: int, highways: List[List[int]], k: int) -> int:
        graph = defaultdict(dict)
        for a, b, c in highways:
            graph[a][b] = c
            graph[b][a] = c

        @lru_cache(None)
        def dfs(cur, explored):
            if explored.bit_count() == k + 1:
                return 0

            ans = -inf
            for other, v in graph[cur].items():
                if not explored & (o := 1 << other):
                    ans = max(ans, dfs(other, explored | o) + v)
            return ans

        return max(-1, max(dfs(i, 1 << i) for i in range(n)))
```
