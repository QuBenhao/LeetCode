# [Python] A new day, a new memoized search or dynamic programming solution

> Author: Benhao
> Date: 2021-06-10
> Upvotes: 10
> Tags: Python, Python3

---

### Approach
Plain exhaustive search without optimization (6484ms)

Greedy pruning (360ms)

For this pruning strategy, first note that once the current count exceeds a known solution, there is no reason to continue searching.
Also, restrict the search to square numbers between the largest square and one quarter of it, using the fact that an integer can be expressed as the sum of four squares.

Search by count (336ms)
The greedy pruning above is less intuitive, but enumerating by the number of terms is easy to understand.

bfs(~200ms)

Unbounded knapsack dynamic programming (~4000ms)


### Code

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
        # Search by count
        for i in range(2,n+1):
            # Among i square terms, at least one must be at least the average n//i
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
