# [Python] 二分法

> Author: Benhao
> Date: 2021-05-23
> Upvotes: 3
> Tags: Python, Python3

---

### 解题思路
因为只能整点发车，但不一定要整点到达。所以最后一个不需要向上取整

### 代码

```python3
class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        def helper(v):
            h = 0.0
            for d in dist[:-1]:
                t = float(d)/v
                h += ceil(t)
            h += float(dist[-1])/v
            return h <= hour
        
        if hour <= len(dist) - 1:
            return -1
        l,r = 1, 10 ** 7
        while l < r:
            mid = (l+r)//2
            if helper(mid):
                r = mid
            else:
                l = mid + 1
        return l
```