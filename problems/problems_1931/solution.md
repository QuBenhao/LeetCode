# [Python] Compress states along the smaller column dimension

> Author: Benhao
> Date: 2021-07-11
> Upvotes: 2
> Tags: Python, Python3

---

### Approach
I made a mistake during the contest and used row-based states, which timed out.

Store the previous m colors in a tuple of length m. Only its first entry (the left neighbor) and last entry (the upper neighbor) affect the current color.

### Code

```python3
class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        @lru_cache(None)
        def dfs(i, j, colors):
            if i == m - 1 and j == n - 1:
                if colors[0] == -1 and colors[-1] == -1:
                    return 3
                elif colors[0] == -1 or colors[-1] == -1:
                    return 2
                return 2 if colors[0] == colors[-1] else 1
            ans = 0
            if i == m - 1:
                tmp = list(colors[1:])
                for k in range(3):
                    if k != colors[0] and k != colors[-1]:
                        ans += dfs(0, j + 1, tuple(tmp + [k]))
            else:
                tmp = list(colors[1:])
                for k in range(3):
                    if (i and k != colors[0] and k != colors[-1]) or (not i and k != colors[0]):
                        ans += dfs(i + 1, j, tuple(tmp + [k]))
            return ans % (10 ** 9 + 7)
        
        return dfs(0, 0, tuple([-1] * m))
```
