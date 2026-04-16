# 深度优先搜索应用题

> Author: Benhao
> Date: 2022-12-04
> Upvotes: 10
> Tags: Go, Java, JavaScript, Python3, TypeScript

---

> Problem: [1774. 最接近目标价格的甜点成本](https://leetcode.cn/problems/closest-dessert-cost/description/)

[TOC]

# 思路
> 按题意搜索答案

# 解题方法
> 深度优先搜索

# 复杂度
- 复杂度: 
> 搜索不讨论时空复杂度

# Code
```Python3 []

class Solution:
    def closestCost(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
        @lru_cache(None)
        def dfs(cur, idx):
            if idx == len(toppingCosts) or cur >= target:
                return cur, abs(cur - target)
            ans, diff = inf, inf
            for i in range(3):
                res = dfs(cur + toppingCosts[idx] * i, idx + 1)
                if res[1] < diff:
                    ans, diff = res
                elif res[1] == diff:
                    ans = min(ans, res[0])
            return ans, diff
        
        r, d = inf, inf
        for b in baseCosts:
            c = dfs(b, 0)
            if c[1] < d:
                r, d = c
            elif c[1] == d:
                r = min(r, c[0])
        return r

```
