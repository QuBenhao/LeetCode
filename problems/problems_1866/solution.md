# [Python] Place the shortest stick at each step

> Author: Benhao
> Date: 2021-05-16
> Upvotes: 13
> Tags: Python, Python3

---

### Approach
Suppose we arrange 5 sticks so that 3 are visible.
If `1` is visible, `1` must be first. We then need arrangements of `2,3,4,5` with exactly `3-1=2` visible sticks.
If `1` is hidden, placing `1` anywhere except first does not change visibility. We then need arrangements of `2,3,4,5` with `3` visible sticks.

Arranging `2,3,4,5` with `3` visible sticks is equivalent to arranging `1,2,3,4` with `3` visible sticks.
Apply the same recurrence again.

That is:
```python3
# With i sticks, the shortest stick has i-1 positions where it is hidden
dp[i][j] = dp[i-1][j-1] + dp[i-1][j] * (i-1)
```
Considering the last stick, as in the official solution, yields the same recurrence.

Use a rolling array

### Code

```python3
class Solution:
    def rearrangeSticks(self, n: int, k: int) -> int:        
        mod = 10 ** 9 + 7

        dp = [0] * (k+1)
        # Base case: one stick
        dp[1] = 1
        for i in range(2, n+1):
            new = [0] * (k+1)
            for j in range(1, k+1):
                # Put the shortest stick first, where it is visible: decrease both the stick count and k by 1
                # Put the shortest stick in any of the other i-1 positions, where it is hidden: decrease the stick count by 1 and keep k unchanged
                new[j] = dp[j-1] + dp[j] * (i-1)
            dp = new
        return dp[k] % mod

```
