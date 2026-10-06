# [Python] Backtracking

> slug: python-hui-su-by-himymben-ghog
> date: 2024-03-10
> tags: C, Go, Java, Python3, TypeScript
> question: Combinations (combinations)
> url: https://leetcode.cn/problems/combinations/solutions/rlebej/python-hui-su-by-himymben-ghog/

---

> Problem: [77. 组合](https://leetcode.cn/problems/combinations/description/)

[TOC]

# Intuition

> Backtracking

# Approach

> Choosing k out of n allows n - k numbers to be skipped in turn.


# Code
```Python3 []
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        path = []
        
        def dfs(x):
            remain = k - len(path)
            if not remain:
                ans.append(list(path))
                return
            if n + 1 - x > remain:
                dfs(x + 1)
            path.append(x)
            dfs(x + 1)
            path.pop()
        
        dfs(1)
        return ans
```
  
