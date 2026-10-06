# [Python] Dynamic programming: O(m * n) time, O(n) space

> Author: Benhao
> Date: 2021-07-18
> Upvotes: 13
> Tags: Python, Python3

---

### Approach
For previous-row positions to the left, add their index and subtract the current index. For positions to the right, subtract their index and add the current index.
Take the maximum for each side.

### Code
```python3
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        m = len(points)
        n = len(points[0])
        dp = points[0]
        for i in range(1, m):
            new_dp = list(dp)
            left_max = -inf
            right_max = -inf
            for j in range(n):
                left_max = max(left_max, dp[j] + j)
                right_max = max(right_max, dp[n-1-j] - (n - 1 - j))
                new_dp[j] = max(left_max - j + points[i][j], new_dp[j])
                new_dp[n-1-j] = max((n - 1 - j) + right_max + points[i][n-1-j], new_dp[n-1-j])
            dp = new_dp
        return max(dp)
```
