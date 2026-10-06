# [Python] Two-dimensional DP or memoized search

> Author: Benhao
> Date: 2021-06-06
> Upvotes: 11
> Tags: Python, Python3

---

### Approach
Let `dp[i][j]` be the maximum number of elements selected using `i zeros and j ones`.

For each s, update the entire DP table in reverse order, since earlier entries can affect later ones but not vice versa.
Any selection whose counts remain within m and n after adding s is valid, though not necessarily optimal.

### Code

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
            # Maximum of selecting and skipping the current idx
            return max(dfs(idx+1, x - zeros, y - ones) + 1, dfs(idx+1, x, y))
        
        l = len(strs)
        return dfs(0, m, n)
```
