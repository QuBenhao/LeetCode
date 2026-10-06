# [Python] Memoized search: 100%

> Author: Benhao
> Date: 2021-05-23
> Upvotes: 3
> Tags: Python, Python3

---

### Approach
Timeouts mainly come from long cases with a blocked run exceeding the maximum jump distance. A method similar to the first problem can reject these as False.
The main fix for the timeout is to return False from the entire DFS early instead of continuing the search.

### Code

```python3
class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        @lru_cache(None)
        def dfs(i):
            if i == n - 1:
                return True
            if s[i] == '1' or n - 1 - i < minJump:
                return False
            for j in range(min(i+maxJump,n-1), i+minJump-1,-1):
                if dfs(j):
                    return True
            return False

        if s[-1] == '1':
            return False
        if len(max(re.split('0+',s),key=len)) >= maxJump:
            return False
        n = len(s)
        return dfs(0)
```
