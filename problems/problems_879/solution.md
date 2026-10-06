# [Python] Memoized search or dynamic programming

> Author: Benhao
> Date: 2021-06-09
> Upvotes: 23
> Tags: Python, Python3

---

### Approach
After all that pruning, I did not expect it to actually pass
The key is that we can often ignore the headcount limit when even all remaining people would not exceed it, or ignore the profit requirement once minProfit has been reached

The search approach translates easily into dynamic programming.

The final inclusion-exclusion approach is the fastest; the idea comes from [this excellent solution](https://leetcode.cn/problems/profitable-schemes/solution/qiao-yong-rong-chi-yuan-li-jian-hua-ti-mu-by-lucif/)

### Code

Memoized search
```python3
class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        @lru_cache(None)
        def dfs(idx, p, pro):
            if idx == len(group):
                return int(pro == minProfit)
            if 0 <= p < group[idx]:
                return dfs(idx+1,p,pro)
            if p >= presum_g[-1] - presum_g[idx]:
                p = inf
            return dfs(idx+1,p-group[idx],min(minProfit, pro+profit[idx]))+dfs(idx+1,p,pro)

        presum_g = list(accumulate([0] + group))

        return dfs(0,n,0) % (10**9+7)
```

DP using Counter
```python3
class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        dp = Counter()
        dp[(0,0)] = 1
        for g,p in zip(group, profit):
            for tg, tp in sorted(dp.keys(),reverse=True):
                if tg + g <= n:
                    dp[(tg+g, min(minProfit, tp+p))] += dp[(tg,tp)]
        return sum(val for (_,v),val in dp.items() if v == minProfit) % (10 ** 9 + 7)
```

DP using SortedDict
```python3
from sortedcontainers import SortedDict


class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        dp = SortedDict()
        dp[(0,0)] = 1
        for g,p in zip(group, profit):
            for tg,tp in list(dp.keys()):
                # Negate tg,tp for sorting
                if g - tg <= n:
                    key = tg-g, -min(p-tp, minProfit)
                    if key in dp:
                        dp[key] += dp[(tg,tp)]
                    else:
                        dp[key] = dp[(tg,tp)]
        return sum(val for (_,v),val in dp.items() if v == -minProfit) % (10 ** 9 + 7)
```

Finally, an implementation based on the expert's inclusion-exclusion idea
```python3
class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        mod = 10 ** 9 + 7

        # Inclusion-exclusion: the count with g <= n, p >= minProfit equals the count with g<=n minus the count with g<=n,p < minProft
        # First count combinations with g<=n
        dp1 = [0] * (n+1)
        dp1[0] = 1
        for g in group:
            for i in range(n,g-1,-1):
                dp1[i] += dp1[i-g]
        # The count of combinations with p < minProfit is 0
        if not minProfit:
            return sum(dp1) % mod
        
        # Count combinations with g <= n, p < minProfit
        dp2 = [[0] * minProfit for _ in range(n+1)]
        dp2[0][0] = 1
        for g,p in zip(group, profit):
            for i in range(n,g-1,-1):
                for j in range(minProfit-1,p-1,-1):
                    dp2[i][j] += dp2[i-g][j-p]
        return (sum(dp1) - sum(sum(dp2[i]) for i in range(n+1))) % mod
```
