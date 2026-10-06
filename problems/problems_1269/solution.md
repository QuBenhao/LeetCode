# [Python] From memoized DFS to bottom-up dynamic programming to a mathematical pattern?

> Author: Benhao
> Date: 2021-05-12
> Upvotes: 14
> Tags: Python, Python3

---

### Approach
lru_cache is unbeatable.

A one-dimensional dp array can implement the same recurrence from the bottom up.
**Observations:**
> A position's next state comes from the previous states at that position and its two neighbors: `dp[j] = dp[j-1] + dp[j] + dp[j+1]`.
>
> The range of `steps` is **much smaller than** `arrLen`! If arrLen is large enough, reaching its end and returning is impossible.
> The farthest position from which we can return is only **half of step** away.
> Thus, use the smaller of `steps//2` and `arrLen` for the dp array length. Updating any excess part of arrLen cannot affect the result.
>
> Initialize the two one-step states to 1, add a 0 at each boundary, and the setup is complete.
>
> A small time optimization: update dp only up to the minimum of `i (the distance reachable so far)`, `steps-i (the distance from which we can return)`, and `the array length`.

**Aside: symmetry in the result** (idea from [曙光磁铁](https://leetcode.cn/problems/number-of-ways-to-stay-in-the-same-place-after-some-steps/solution/ostepssuan-fa-zai-xian-qiu-jiao-shu-xue-mz6i2/))
> Working backward from the final row is the same as working forward from the initial row: the processes are symmetric.
>
> For example, with steps = 6, arrLen = 4:
> 
> The result is as follows. In each product, the left factor is a value resembling an entry in Pascal's triangle; the right factor counts how often it contributes to the final answer.
>
> 51 * 1 (sixth row) 
> 
>   = 21 * 1 + 30 * 1 (fifth row)
> 
>    = 9 * 2 + 12 * 2 + 9 * 1 (fourth row)
> 
>    = 4 * 4 + 5 * 5 + 3 * 3 + 1 * 1 (the middle row)
>
>    = 2 * 9 + 2 * 12 + 1 * 9 (the products at symmetric positions now appear in reverse order)
> 
>    = 1 * 21 + 1 * 30 (second row)
>
>    = 1 * 51 (initial row)
>
> We can therefore compute dp only through half of step (the middle row), then calculate the final result directly.
> 
> This runtime already consistently beats 100%; an O(1) formula, if derived, would be even faster.


### Code

```python3
class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        @lru_cache(None)
        def dfs(cur, s):
            if cur == -1 or cur == arrLen or cur > s:
                return 0
            if cur <= 1 and s == 1:
                return 1
            s -= 1
            return dfs(cur, s) + dfs(cur-1,s) + dfs(cur+1,s)

        return dfs(0, steps) % (10 ** 9 + 7)
```
Bottom-up dp
```python3
class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        # One-dimensional dynamic programming with bottom-up rolling updates
        if arrLen == 1 or steps == 1:
            return 1
        dp = [0] * (min(steps // 2 + 1, arrLen) + 2)
        n = len(dp)
        dp[1] = dp[2] = 1
        for i in range(1, steps):
            nxt_dp = [0] * n
            for j in range(1, min(n - 1, i + 3, steps - i + 1)):
                nxt_dp[j] = dp[j-1] + dp[j] + dp[j+1]
            dp = nxt_dp
        return dp[1] % (10 ** 9 + 7)
```

Use the mathematical pattern to compute only half the dp rows. I have not yet found a formula for the result directly.
```python3
class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        # One-dimensional dynamic programming with bottom-up rolling updates
        if arrLen == 1 or steps == 1:
            return 1
        dp = [0] * (min(steps // 2 + 1, arrLen) + 2)
        n = len(dp)
        dp[1] = dp[2] = 1
        # Symmetry: dp at half of steps is enough, because working back toward position 0 is the same as working forward from position 0
        for i in range(1, steps // 2):
            nxt_dp = [0] * n
            for j in range(1, min(n - 1, i + 3)):
                nxt_dp[j] = dp[j-1] + dp[j] + dp[j+1]
            dp = nxt_dp
        # An even-numbered row is the sum of squares of its middle row
        if steps % 2 == 0:
            return sum(x**2 for x in dp) % (10 ** 9 + 7)
        # An odd-numbered row is the dot product of its two middle rows
        return sum(dp[i] * (dp[i-1] + dp[i] + dp[i+1]) for i in range(1,len(dp)-1)) % (10 ** 9 + 7)
```
