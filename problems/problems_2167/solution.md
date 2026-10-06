# [Python] Dynamic programming with prefixes and suffixes

> slug: python-qian-zhui-hou-zhui-si-xiang-de-do-rz7v
> date: 2022-02-06
> tags: Python, Python3
> question: Minimum Time to Remove All Cars Containing Illegal Goods (minimum-time-to-remove-all-cars-containing-illegal-goods)
> url: https://leetcode.cn/problems/minimum-time-to-remove-all-cars-containing-illegal-goods/solutions/J0SM0I/python-qian-zhui-hou-zhui-si-xiang-de-do-rz7v/

---
### Approach
I learned from [灵老师's solution](https://leetcode.cn/problems/minimum-time-to-remove-all-cars-containing-illegal-goods/solution/qian-hou-zhui-fen-jie-dp-by-endlesscheng-6u1b/); I did not think of this state transition during the contest.

### Code

```python3
class Solution:
    def minimumTime(self, s: str) -> int:
        n, cur, ans = len(s), 0, inf
        # cur: minimum cost to remove through i from the left; dp: minimum cost to remove through i from the right
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

For the optimization, see [@megurine](/u/megurine/). Only consider removals from the left, assuming the right side has already been removed up to the current position.
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
