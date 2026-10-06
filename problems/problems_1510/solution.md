# [Python] Memoized search or dynamic programming (less space) or memoized recursion (one line)

> Author: Benhao
> Date: 2021-06-16
> Upvotes: 4
> Tags: Python, Python3

---

### Approach
You win if you can force your opponent to lose; otherwise, you lose.

### Code

```python3
class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        @lru_cache(None)
        def dfs(curr):
            if not curr:
                return False
            for i in range(int(math.sqrt(curr)),0,-1):
                if not dfs(curr-i*i):
                    return True
            return False

        return dfs(n)
```
Store all False states in a set (or all True states). Subtract each possible square and check set membership to determine whether the current state belongs in the set.
```python3
class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        dp = {0}
        for i in range(1, n+1):
            if all(i-j*j not in dp for j in range(int(math.sqrt(i)), 0, -1)):
                dp.add(i)
        return n not in dp
```

```python3
class Solution:
    @lru_cache(None)
    def winnerSquareGame(self, n: int) -> bool:
        return True if n > 0 and any(not self.winnerSquareGame(n-i*i) for i in range(int(sqrt(n)),0,-1)) else False
```
