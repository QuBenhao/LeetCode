# [Python] 记忆化搜索 or 动态规划

> Author: Benhao
> Date: 2021-06-09
> Upvotes: 23
> Tags: Python, Python3

---

### 解题思路
剪了半天枝,没想到真能过
其实关键在于很多时候我们可以忽略人数限制(加上后面所有人也不会超)，或者忽略profit限制了(已经达到minProfit了)

根据搜索的思路很容易写出动态规划。

最后的容斥原理是最快的,思路来自[大佬的题解](https://leetcode.cn/problems/profitable-schemes/solution/qiao-yong-rong-chi-yuan-li-jian-hua-ti-mu-by-lucif/)

### 代码

记忆化搜索
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

dp使用Counter
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

dp使用SortedDict
```python3
from sortedcontainers import SortedDict


class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        dp = SortedDict()
        dp[(0,0)] = 1
        for g,p in zip(group, profit):
            for tg,tp in list(dp.keys()):
                # tg,tp为负为了排序
                if g - tg <= n:
                    key = tg-g, -min(p-tp, minProfit)
                    if key in dp:
                        dp[key] += dp[(tg,tp)]
                    else:
                        dp[key] = dp[(tg,tp)]
        return sum(val for (_,v),val in dp.items() if v == -minProfit) % (10 ** 9 + 7)
```

最后，根据大佬的容斥原理思路写的
```python3
class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        mod = 10 ** 9 + 7

        # 容斥原理 g <= n, p >= minProfit的组合个数为 g<=n的个数减去g<=n,p < minProft的个数
        # 先求 g<=n 的组合数
        dp1 = [0] * (n+1)
        dp1[0] = 1
        for g in group:
            for i in range(n,g-1,-1):
                dp1[i] += dp1[i-g]
        # p < minProfit的组合数为0
        if not minProfit:
            return sum(dp1) % mod
        
        # 求 g <= n, p < minProfit的组合数
        dp2 = [[0] * minProfit for _ in range(n+1)]
        dp2[0][0] = 1
        for g,p in zip(group, profit):
            for i in range(n,g-1,-1):
                for j in range(minProfit-1,p-1,-1):
                    dp2[i][j] += dp2[i-g][j-p]
        return (sum(dp1) - sum(sum(dp2[i]) for i in range(n+1))) % mod
```