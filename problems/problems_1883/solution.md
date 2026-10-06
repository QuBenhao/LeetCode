# [Python] Dynamic programming

> Author: Benhao
> Date: 2021-05-30
> Upvotes: 1
> Tags: Python, Python3

---

### Approach
Based on [this code](https://leetcode.com/problems/minimum-skips-to-arrive-at-meeting-on-time/discuss/1239772/Python-dp-O(n2))
See the comments for an explanation.

### Code

```python3
class Solution:
    def minSkips(self, dist: List[int], speed: int, hoursBefore: int) -> int:
        eps = 1e-9
        n = len(dist)
        dp = [[10**7+1] * (n+1) for _ in range(n+1)]
        dp[0][0] = 0
        for i,d in enumerate(dist, 1):
            # Skip no rests
            dp[i][0] = ceil(dp[i-1][0] + d/speed - eps)
            # At i, at most i rests can have been skipped
            for j in range(1, i+1):
                # For j skips, either skip now after j-1 earlier skips or rest now after j earlier skips
                dp[i][j] = min(dp[i-1][j-1] + d/speed, ceil(dp[i-1][j] + d/speed - eps))
        
        for j,t in enumerate(dp[-1]):
            # Scan left to right for the minimum skips that allow an on-time arrival
            if t <= hoursBefore:
                return j
        return -1

```
