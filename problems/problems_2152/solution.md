# [Python] 状压 + 记忆化递归

> slug: python-zhuang-ya-ji-yi-hua-di-gui-by-him-ghw8
> date: 2022-04-26
> tags: Python, Python3
> question: Minimum Number of Lines to Cover Points (minimum-number-of-lines-to-cover-points)
> url: https://leetcode.cn/problems/minimum-number-of-lines-to-cover-points/solutions/lqHI2T/python-zhuang-ya-ji-yi-hua-di-gui-by-him-ghw8/

---
### 解题思路
枚举点是否有直线了，再枚举没有直线的点和其他点组成直线

### 代码

```python3
class Solution:
    def minimumLines(self, points: List[List[int]]) -> int:
        n = len(points)
        total = (1 << n) - 1
        
        def is_line(p1, p2, p3):
            x1, y1 = p1
            x2, y2 = p2
            x3, y3 = p3
            return (x2-x1) * (y3-y1) == (x3-x1) * (y2-y1)

        @lru_cache(None)
        def dfs(state):
            if state == total:
                return 0
            ans = inf
            for i in range(n):
                if not (1 << i) & state:
                    nxt_state = state | 1 << i
                    for j in range(i + 1, n):
                        cur = nxt_state | 1 << j
                        for other in range(j + 1, n):
                            if not (1 << other) & cur and is_line(points[i], points[j], points[other]):
                                cur |= 1 << other
                        ans = min(ans, dfs(cur) + 1)
                    if i == n - 1:
                        ans = min(ans, dfs(nxt_state) + 1)
            return ans
        
        return dfs(0)
```