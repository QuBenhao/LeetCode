# [Python] 记忆化搜索 or 动态规划(省空间) or 记忆化递归(一行)

> Author: Benhao
> Date: 2021-06-16
> Upvotes: 4
> Tags: Python, Python3

---

### 解题思路
能使对方输就是自己赢，不能使对方输就是自己输

### 代码

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
使用集合记录所有False(也可以记录所有True)，判断与各种平方数的差值在不在集合中就知道当前值在不在集合中了
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