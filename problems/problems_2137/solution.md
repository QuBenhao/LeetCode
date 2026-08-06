# [Python] 二分

> slug: python-er-fen-by-himymben-zhba
> date: 2022-04-28
> tags: Python, Python3
> question: Pour Water Between Buckets to Make Water Levels Equal (pour-water-between-buckets-to-make-water-levels-equal)
> url: https://leetcode.cn/problems/pour-water-between-buckets-to-make-water-levels-equal/solutions/y6r0JA/python-er-fen-by-himymben-zhba/

---
### 解题思路
此处撰写解题思路

### 代码

```python3
class Solution:
    def equalizeWater(self, buckets: List[int], loss: int) -> float:
        n, l, r, s = len(buckets), 0, max(buckets), sum(buckets)

        def helper(x):
            s1 = s2 = 0
            for b in buckets:
                if b > x:
                    # 倒掉了多少水
                    s1 += b - x
                else:
                    # 至少需要多少水
                    s2 += (x - b) * 100 / (100 - loss)
            return s1 >= s2

        while (r - l) > 1e-5:
            mid = (l + r) / 2
            if helper(mid):
                l = mid
            else:
                r = mid - 0.000001
        return l
```