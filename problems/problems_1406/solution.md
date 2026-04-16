# [Python] 记忆化搜索 or 动态规划(优化双100%)

> Author: Benhao
> Date: 2021-06-16
> Upvotes: 1
> Tags: Python, Python3

---

### 解题思路
找每个idx能取到的最大值即可

使用三个变量记录最近的三个dp值，滚动更新，优化为空间O(1)

### 代码

```python3
class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        @lru_cache(None)
        def dfs(idx):
            if idx == n:
                return 0
            res = -inf
            for i in range(idx+1,min(n+1,idx+4)):
                res = max(res, presum[i] - presum[idx] - dfs(i))
            return res

        n = len(stoneValue)
        presum = list(accumulate([0] + stoneValue))
        ans = dfs(0)
        if ans > 0:
            return "Alice"
        elif ans == 0:
            return "Tie"
        else:
            return "Bob"
```

```python3
class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        presum = list(accumulate([0] + stoneValue))
        dp = [0] * (n + 3)
        for i in range(n-1,-1,-1):
            dp[i] = presum[-1] - presum[i] - min(dp[j] for j in range(i+1,i+4))
        ans = dp[0] * 2 - presum[-1]
        if ans > 0:
            return "Alice"
        elif ans == 0:
            return "Tie"
        else:
            return "Bob"
```

```python3
class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        curr_sum = 0
        # 滚动更新
        dp0 = dp1 = dp2 = 0
        # 倒序递推
        for i in range(n-1,-1,-1):
            curr_sum += stoneValue[i]
            dp0, dp1, dp2 = curr_sum - min(dp0, dp1, dp2), dp0, dp1
        # Alice的分数减去Bob的分数
        ans = dp0 * 2 - curr_sum
        if ans > 0:
            return "Alice"
        elif ans == 0:
            return "Tie"
        else:
            return "Bob"
```