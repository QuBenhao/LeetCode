# [Python] 前缀后缀思想的动态规划

> slug: python-qian-zhui-hou-zhui-si-xiang-de-do-rz7v
> date: 2022-02-06
> tags: Python, Python3
> question: Minimum Time to Remove All Cars Containing Illegal Goods (minimum-time-to-remove-all-cars-containing-illegal-goods)
> url: https://leetcode.cn/problems/minimum-time-to-remove-all-cars-containing-illegal-goods/solutions/J0SM0I/python-qian-zhui-hou-zhui-si-xiang-de-do-rz7v/

---
### 解题思路
学习的[灵老师的题解](https://leetcode.cn/problems/minimum-time-to-remove-all-cars-containing-illegal-goods/solution/qian-hou-zhui-fen-jie-dp-by-endlesscheng-6u1b/)，比赛时没有想到做这样的转移处理。

### 代码

```python3
class Solution:
    def minimumTime(self, s: str) -> int:
        n, cur, ans = len(s), 0, inf
        # cur: 从左边删到i的最小代价, dp: 从右边删到i的最小代价
        dp = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            if s[i] == '0':
                dp[i] = dp[i + 1]
            else:
                dp[i] = min(n - i, dp[i + 1] + 2)
        for i in range(n):
            ans = min(ans, cur + dp[i])
            if s[i] == '1':
                cur = min(i + 1, cur + 2)
        return min(ans, cur)
```

优化参考[@megurine](/u/megurine/)，讨论从左删即可，默认右边删到了当前位置
```python3
class Solution:
    def minimumTime(self, s: str) -> int:
        n, ans, l = len(s), inf, 0
        for i, c in enumerate(s):
            if c == '1':
                l = min(i + 1, l + 2)
            ans = min(ans, l + n - 1 - i)
        return ans
```