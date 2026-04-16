# [Python] 记忆化搜索

> Author: Benhao
> Date: 2024-05-07
> Upvotes: 1
> Tags: C, Go, Java, Python3, TypeScript

---


> Problem: [1463. 摘樱桃 II](https://leetcode.cn/problems/cherry-pickup-ii/description/)

[TOC]

# 思路

同[昨天的摘樱桃](https://leetcode.cn/problems/cherry-pickup/solutions/2767715/pythongo-ji-yi-hua-di-gui-dong-tai-gui-h-i3tm/)


# Code
```Python3 []
class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        @lru_cache(None)
        def dfs(step, i1, i2):
            if i1 > i2:
                return dfs(step, i2, i1)
            ans, cur = 0, grid[step][i1] + grid[step][i2] - (i1 == i2) * grid[step][i1]
            if step == m - 1:
                return cur
            for nxt_i1, nxt_i2 in product(range(max(0, i1 - 1), min(n, i1 + 2)), range(max(0, i2 - 1), min(n, i2 + 2))):
                ans = max(ans, cur + dfs(step + 1, nxt_i1, nxt_i2))
            return ans
        return dfs(0, 0, n - 1)
```
  
