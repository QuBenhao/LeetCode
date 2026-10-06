# [Python] Memoized DFS, beats 100%

> Author: Benhao
> Date: 2021-05-04
> Upvotes: 4
> Tags: Python, Python3

---

### Approach
DFS with a little backtracking.

Pass the house index, color, and number of remaining neighborhoods to dfs.
(Keep houses as an external list that is updated as needed, rather than passing it as an argument: a list would need a hash representation for lru_cache. Use backtracking to restore the corresponding house value.)

For pruning, a negative number of remaining neighborhoods (that is, -1) makes the assignment invalid. More remaining neighborhoods than remaining houses is also invalid.

For unpainted houses, try every color. For painted houses, update the number of remaining neighborhoods and pass it downward.


### Code

```python3
class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        @lru_cache(None)
        def dfs(idx, color, t):
            if t < 0 or t > m - idx:
                return float("inf")
            if idx == m:
                return 0
            curr = float("inf")
            if houses[idx]:
                if idx:
                    if houses[idx] != houses[idx - 1]:
                        curr = min(curr, dfs(idx + 1, houses[idx], t - 1))
                    else:
                        curr = min(curr, dfs(idx + 1,houses[idx], t))
                else:
                    curr = min(curr, dfs(idx + 1, houses[idx], t - 1))
            else:
                for i in range(1,n+1):
                    houses[idx] = i
                    if idx > 0:
                        if i != houses[idx-1]:
                            curr = min(curr, dfs(idx + 1,houses[idx], t - 1) + cost[idx][i-1])
                        else:
                            curr = min(curr, dfs(idx + 1,houses[idx], t) + cost[idx][i-1])
                    else:
                        curr = min(curr, dfs(idx + 1,houses[idx], t - 1) + cost[idx][i-1])
                houses[idx] = 0
            return curr

        res = dfs(0, 0, target)
        if res == float("inf"):
            return -1
        return res
```

Using color instead of houses[idx-1] makes the code shorter and faster, and removes the need to assign values to houses.
```python3
class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        @lru_cache(None)
        def dfs(idx, color, t):
            if t < 0 or t > m - idx:
                return float("inf")
            if idx == m:
                return 0
            curr = float("inf")
            if houses[idx]:
                if houses[idx] != color:
                    curr = min(curr, dfs(idx + 1, houses[idx], t - 1))
                else:
                    curr = min(curr, dfs(idx + 1, houses[idx], t))
            else:
                for i in range(1, n + 1):
                    if i != color:
                        curr = min(curr, dfs(idx + 1, i, t - 1) + cost[idx][i - 1])
                    else:
                        curr = min(curr, dfs(idx + 1, i, t) + cost[idx][i - 1])
            return curr

        res = dfs(0, 0, target)
        if res == float("inf"):
            return -1
        return res
```
