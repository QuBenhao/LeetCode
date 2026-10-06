# [Python] DP + binary search

> Author: Benhao
> Date: 2022-10-22
> Upvotes: 13
> Tags: Go, Java, JavaScript, Python, Python3, TypeScript

---

### Approach
Sort by end time. The maximum profit at each position comes from either `the previous maximum profit (skip the current job)` or `the current job plus the maximum earlier profit compatible with it`.
To locate the last compatible job, use binary search to find where the current start time falls among the sorted end times.

### Code

```Python3 
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs, dp = sorted(zip(endTime, startTime, profit)), [0] * (len(startTime) + 1)
        for i, (end, start, pf) in enumerate(jobs):
            dp[i + 1] = max(dp[i], dp[bisect_right(jobs, start, key=lambda x:x[0])] + pf)
        return dp[-1]
```
