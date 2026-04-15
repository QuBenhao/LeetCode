# [Python] 二分查找 or 贪心

> Author: Benhao
> Date: 2021-05-28
> Upvotes: 2
> Tags: Python, Python3

---

### 解题思路
首先所有tasks里面的`cost`都是要被减掉的，那么答案至少是这些`cost`的和。
要使得总和尽可能地小，那么最终`minimum`和`cost`的差距要尽可能地小，所以想到根据两者之差排序。
然后发现好像不用二分查找，直接贪心就可以了。

**贪心的证明:**
先紧着差距小的来。这样res的更新总是当前所需的最小值。
dp[i]代表取到i位置时需要的最小值。
显然dp[i+1]最少也是要dp[i]+actual的，而i+1又对当前位置至少要取到有限制，
故: 
```Python3
dp[i+1] = max(dp[i] + actual, minimum)
```

详细贪心的证明见[这里](https://leetcode.cn/problems/minimum-initial-energy-to-finish-tasks/solution/wan-cheng-suo-you-ren-wu-de-zui-shao-chu-shi-neng-/)，写的很好。

### 代码

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