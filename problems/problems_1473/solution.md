# [Python] 记忆化DFS 100%

> Author: Benhao
> Date: 2021-05-04
> Upvotes: 4
> Tags: Python, Python3

---

### 解题思路
dfs加点儿backtracking

以房间号、对应颜色和剩余街区作为dfs传参
(houses列表作为外部变量，不断改变而不作为传参，因为list还要给lru_cache设计hash，使用backtracking回退house对应的值即可)

关于剪枝，当剩余街区小于0（也就是-1），说明分配不合理；当剩余街区比剩余的房子还多，也是分配不合理的；

剩下的就是对没有颜色的房子遍历找颜色，对有颜色的统计一下剩余街区往下传即可。


### 代码

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

使用color代替houses[idx-1]的使用，代码更简洁也更快了。(不需要再对houses赋值了)
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