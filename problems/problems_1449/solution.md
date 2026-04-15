# [Python] 记忆化dfs or 动态规划

> Author: Benhao
> Date: 2021-06-12
> Upvotes: 11
> Tags: Python, Python3

---

### 解题思路
按贪心先搜代价最小的(这样组出的长度更长)，数值更大的(这样组出的数字更大)。

### 代码

```python3
class Solution:
    def largestNumber(self, cost: List[int], target: int) -> str:
        @lru_cache(None)
        def dfs(curr):
            if not curr:
                return ""
            ans = "0"
            for val in cost:
                if curr >= val:
                    res = dfs(curr - val)
                    if res != '0':
                        if ans == '0' or len(res) + 1 > len(ans):
                            ans = d[val] + res
                        elif len(res) + 1 == len(ans):
                            ans = max(ans, d[val] + res, key=int)
            return str(ans)

        # 重复的代价永远会取更高的那个
        d = dict((v,str(i)) for i,v in enumerate(cost,1))
        cost = sorted(d.keys())
        return dfs(target)
```

```python3
class Solution:
    def largestNumber(self, cost: List[int], target: int) -> str:
        d = dict((v,str(i)) for i,v in enumerate(cost,1))
        dp = [''] + ['0'] * target
        for i in range(target+1):
            for k,v in d.items():
                if i >= k and dp[i-k] != '0':
                    dp[i] = max(dp[i], v+dp[i-k], key=int)
        return dp[target]
```