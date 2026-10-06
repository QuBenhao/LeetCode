# [Python] Dynamic programming

> Author: Benhao
> Date: 2021-06-17
> Upvotes: 2
> Tags: Python, Python3

---

### Approach
Memoized search keeps timing out here because top-down visits more states than bottom-up.

Memoizing prefix sums is not enough; storing interval sums in a 2D array just manages to pass.

### Code

```python3
class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
        n = len(stones)
        dp = [[0] * n for _ in range(n)]
        presum = [0] + list(accumulate(stones))
        for length in range(2, n+1):
            for i in range(n - length + 1):
                j = i + length - 1
                dp[i][j] = max(presum[j+1] - presum[i+1] - dp[i+1][j], presum[j] - presum[i] - dp[i][j-1])
        return dp[0][n-1]
```

```python3
class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
        @lru_cache(None)
        def dfs(i, j):
            if i == j:
                return 0
            return max(presum[i+1][j] - dfs(i+1,j), presum[i][j-1] - dfs(i,j-1))
        
        n = len(stones)
        pres = [0] + list(accumulate(stones))
        presum = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                presum[i][j] = pres[j+1] - pres[i]
        dfs.cache_clear()
        return dfs(0, n-1)
```
