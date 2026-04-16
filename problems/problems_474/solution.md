# [Python] 二维dp or 记忆化搜索

> Author: Benhao
> Date: 2021-06-06
> Upvotes: 11
> Tags: Python, Python3

---

### 解题思路
令`dp[i][j]`表示`选了i个0,j个1`的最大元素个数。

那么对于每个s，我们就更新整个dp表格(倒着更新因为前面的会影响后面，但后面不会影响前面）。
所有加入s后个数分别不超过m,n都是合理的（但不一定是最优解法）。

### 代码

```python3
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0] * (n+1) for _ in range(m+1)]
        for s in strs:
            ones = s.count('1')
            zeros = len(s) - ones
            if ones > n or zeros > m:
                continue
            for i in range(m-zeros,-1,-1):
                for j in range(n-ones,-1,-1):
                    dp[i+zeros][j+ones] = max(dp[i+zeros][j+ones], dp[i][j] + 1)
        return dp[m][n]

```

```python3
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        @lru_cache(None)
        def dfs(idx, x, y):
            if x < 0 or y < 0:
                return float("-inf")
            if idx == l:
                return 0
            ones = strs[idx].count('1')
            zeros = len(strs[idx]) - ones
            # 选当前idx和不选当前idx的最大值
            return max(dfs(idx+1, x - zeros, y - ones) + 1, dfs(idx+1, x, y))
        
        l = len(strs)
        return dfs(0, m, n)
```