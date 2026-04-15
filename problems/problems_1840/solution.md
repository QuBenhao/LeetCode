# [Python] 参考别人写了注释

> Author: Benhao
> Date: 2021-04-25
> Upvotes: 6
> Tags: Python

---

### 解题思路
比赛时想到了要用左右边来推中间能达到的最大高度，想到了从左边推算restriction是否合理，却没有想到从右边往左。

### 代码

```python3
class Solution:
    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        restrictions.extend([[1,0],[n,n-1]])
        restrictions.sort()
        m = len(restrictions)
        # 思路的核心在于：如何使restriction中的所有限制合法化(或者说有效)
        # 右边界限制的高度
        for i in range(m - 2, -1, -1):
            restrictions[i][1] = min(restrictions[i][1], restrictions[i+1][1] + restrictions[i+1][0] - restrictions[i][0])
        # 左边界限制的高度
        for i in range(1, m):
            restrictions[i][1] = min(restrictions[i][1], restrictions[i - 1][1] + restrictions[i][0] - restrictions[i-1][0])

        ans = 0
        for i in range(1, m):
            l, limit_l = restrictions[i-1]
            r, limit_r = restrictions[i]
            # 根据左右限制，可以推算出最大高度
            # 根据 h_max - limit_l <= max_idx - l, h_max - limit_r <= r - max_idx
            # 两式相加可得，h_max <= (r - l + limit_r + limit_l) // 2
            ans = max(ans, (r + limit_l + limit_r - l) // 2)
        return ans

```