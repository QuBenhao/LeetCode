# [Python] 动态规划 时间O(m * n)，空间O(n)

> Author: Benhao
> Date: 2021-07-18
> Upvotes: 13
> Tags: Python, Python3

---

### 解题思路
对于所有上一行左边的数，都是加上它的坐标减去自己的坐标；对于上一行所有右边的数，都是减去它的坐标加上自己的坐标；
分别求最大值即可。

### 代码
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