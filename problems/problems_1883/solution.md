# [Python] 动态规划

> Author: Benhao
> Date: 2021-05-30
> Upvotes: 1
> Tags: Python, Python3

---

### 解题思路
参考自[代码](https://leetcode.com/problems/minimum-skips-to-arrive-at-meeting-on-time/discuss/1239772/Python-dp-O(n2))
解释见注释。

### 代码

```python3
class Solution:
    def minSkips(self, dist: List[int], speed: int, hoursBefore: int) -> int:
        eps = 1e-9
        n = len(dist)
        dp = [[10**7+1] * (n+1) for _ in range(n+1)]
        dp[0][0] = 0
        for i,d in enumerate(dist, 1):
            # 全都不跳跃
            dp[i][0] = ceil(dp[i-1][0] + d/speed - eps)
            # 到i的时候最多跳跃i次
            for j in range(1, i+1):
                # 跳跃j次是 本次跳跃，上次跳了j-1次 和 本次不跳跃，上次跳了j次 的递推
                dp[i][j] = min(dp[i-1][j-1] + d/speed, ceil(dp[i-1][j] + d/speed - eps))
        
        for j,t in enumerate(dp[-1]):
            # 从左到右，最小的满足时间内到达的跳跃次数
            if t <= hoursBefore:
                return j
        return -1

```