# [Python] Binary search or greedy

> Author: Benhao
> Date: 2021-05-28
> Upvotes: 2
> Tags: Python, Python3

---

### Approach
Every task's `cost` must be spent, so the answer is at least the sum of all `cost` values.
To minimize the total, the final gap between `minimum` and `cost` should be as small as possible, suggesting sorting by their difference.
It turns out binary search is unnecessary; a greedy approach works directly.

**Greedy proof:**
Process smaller gaps first. Each update to res then gives the minimum currently required.
dp[i] represents the minimum needed through position i.
dp[i+1] must be at least dp[i]+actual, while task i+1 also imposes its own minimum requirement.
Thus:
```Python3
dp[i+1] = max(dp[i] + actual, minimum)
```

See [this explanation](https://leetcode.cn/problems/minimum-initial-energy-to-finish-tasks/solution/wan-cheng-suo-you-ren-wu-de-zui-shao-chu-shi-neng-/) for a detailed, well-written greedy proof.

### Code

```python3
class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        def helper(val):
            for c,m in tasks:
                if val < m:
                    return False
                val -= c
            return True

        tasks.sort(key=lambda x:(x[0] - x[1], x[0], -x[1]))
        l, r = 1, 10 ** 9
        while l < r:
            mid = (l + r) // 2
            if helper(mid):
                r = mid
            else:
                l = mid + 1
        return l
```

```python3
class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        tasks.sort(key=lambda x:(x[1] - x[0]))
        res = 0
        for c,m in tasks:
            res = max(res + c, m)
        return res
```
