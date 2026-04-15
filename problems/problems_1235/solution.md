# [Python] DP + 二分

> Author: Benhao
> Date: 2022-10-22
> Upvotes: 13
> Tags: Go, Java, JavaScript, Python, Python3, TypeScript

---

### 解题思路
按结束时间排序,每个位置的最大收益由`上一次最大收益(不选当前)`和`选当前以及上一次和当前不冲突的最大收益`,
为求得上一次与当前不冲突的位置, 我们采用二分找到开始时间在结束时间所在的坐标即可

### 代码

```Python3 
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs, dp = sorted(zip(endTime, startTime, profit)), [0] * (len(startTime) + 1)
        for i, (end, start, pf) in enumerate(jobs):
            dp[i + 1] = max(dp[i], dp[bisect_right(jobs, start, key=lambda x:x[0])] + pf)
        return dp[-1]
```