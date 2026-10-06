# [Python] Memoized recursion

> slug: python-ji-yi-hua-di-gui-by-himymben-5kvy
> date: 2022-05-08
> tags: Python, Python3
> question:  Check if There Is a Valid Parentheses String Path (check-if-there-is-a-valid-parentheses-string-path)
> url: https://leetcode.cn/problems/check-if-there-is-a-valid-parentheses-string-path/solutions/yE9IJy/python-ji-yi-hua-di-gui-by-himymben-5kvy/

---
### Approach
Track the difference between opening and closing parenthesis counts at (i,j). Return True only if 0 is reachable at the bottom-right corner.

### Code

```python3
DIRS = (0, 1), (1, 0)
class Solution:
    def hasValidPath(self, grid: List[List[str]]) -> bool:
        m, n = len(grid), len(grid[0])

        @lru_cache(None)
        def dfs(i, j, l):
            if l < 0 or l > m + n - 2 - i - j:
                return False
            if i == m - 1 and j == n - 1:
                return l == 0
            for dx, dy in DIRS:
                if (nx := i + dx) < m and (ny := j + dy) < n:
                    if dfs(nx, ny, l + (1 if grid[nx][ny] == '(' else -1)):
                        return True
            return False
        
        return (m + n) % 2 == 1 and grid[0][0] == '(' and grid[m - 1][n - 1] == ')' and dfs(0, 0, 1)
```
