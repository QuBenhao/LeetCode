# [Python] 新的一天,新的记忆化搜索 or 动态规划

> Author: Benhao
> Date: 2021-06-10
> Upvotes: 10
> Tags: Python, Python3

---

### 解题思路
纯硬搜无优化 (6484ms)

贪心剪枝(360ms)

关于这里剪枝的原理，首先我们在统计过程中，已经超过已知的解法的话，就没有搜的必要了。
另外，搜索范围卡在最大的平方数到它的四分之一(本质是使用了一个数可以拆成四个平方数的和的思想)。

次数筛(336ms)
上面贪心的剪枝比较不容易想到，但是按个数遍历就很好理解。

bfs(~200ms)

完全背包动态规划(~4000ms)


### 代码

```python3
class Solution:
    @lru_cache(None)
    def numSquares(self, n: int) -> int:
        if n == 0:
            return 0
        rg = int(sqrt(n))
        ans = inf
        for i in range(rg,0,-1):
            ans = min(ans, self.numSquares(n-i*i) + 1)
        return ans

```

```python3
class Solution:
    ans = inf
    def numSquares(self, n: int) -> int:
        return self.answer(n, 0)

    @lru_cache(None)
    def answer(self, n, ans):
        if ans >= self.ans:
            return inf
        if n == 0:
            self.ans = ans
            return ans
        rg = int(sqrt(n))
        res = inf
        for i in range(rg, rg//2, -1):
            res = min(res, self.answer(n - i * i, ans + 1))
        return res
```

```python3
class Solution:
    @lru_cache(None)
    def numSquares(self, n: int) -> int:
        if n == int(sqrt(n)) ** 2:
            return 1
        # 次数筛
        for i in range(2,n+1):
            # 次数i对应的平方数至少有一个大于等于平均数n//i
            for j in range(int(sqrt(n//i)), int(sqrt(n))+1):
                if self.numSquares(n-j*j) + 1 == i:
                    return i
        return n
```

```python3
class Solution:
    def numSquares(self, n: int) -> int:
        frontier = deque([n])
        explored = set()
        step = 0
        while frontier:
            nxt = []
            for v in frontier:
                for i in range(1, int(sqrt(v))+1):
                    if v-i*i not in explored:
                        if v - i * i == 0:
                            return step + 1
                        nxt.append(v-i*i)
                        explored.add(v-i*i)
            frontier = deque(nxt)
            step += 1
        return n
```

```python3 []
class Solution:
    def numSquares(self, n: int) -> int:
        dp = [0] + [inf] * n
        rg = int(sqrt(n))
        for i in range(1, rg + 1):
            curr = i * i
            for j in range(curr,n+1):
                dp[j] = min(dp[j],dp[j-curr]+1)
        return dp[n]
```
```Go []
const inf int = 0x3f3f3f
func numSquares(n int) int {
    dp := make([]int, n + 1)
    for i := 1; i <= n; i++ {
        dp[i] = inf
        for j := 1; j * j <= i; j++ {
            dp[i] = min(dp[i], dp[i - j * j] + 1)
        }
    }
    return dp[n]
}

func min(a, b int) int {
    if a < b {
        return a
    }
    return b
}
```