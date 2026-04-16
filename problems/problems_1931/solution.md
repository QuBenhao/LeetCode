# [Python] 列数少所以按列状压

> Author: Benhao
> Date: 2021-07-11
> Upvotes: 2
> Tags: Python, Python3

---

### 解题思路
比赛的时候傻了。。。写了个按行的TLE了

用长度为m的tuple记录前面m个位置的颜色分布。影响当前填色的只有第一个(当前的左边格)和最后一个（当前的上边格）

### 代码

```python3
class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        @lru_cache(None)
        def dfs(i, j, colors):
            if i == m - 1 and j == n - 1:
                if colors[0] == -1 and colors[-1] == -1:
                    return 3
                elif colors[0] == -1 or colors[-1] == -1:
                    return 2
                return 2 if colors[0] == colors[-1] else 1
            ans = 0
            if i == m - 1:
                tmp = list(colors[1:])
                for k in range(3):
                    if k != colors[0] and k != colors[-1]:
                        ans += dfs(0, j + 1, tuple(tmp + [k]))
            else:
                tmp = list(colors[1:])
                for k in range(3):
                    if (i and k != colors[0] and k != colors[-1]) or (not i and k != colors[0]):
                        ans += dfs(i + 1, j, tuple(tmp + [k]))
            return ans % (10 ** 9 + 7)
        
        return dfs(0, 0, tuple([-1] * m))
```