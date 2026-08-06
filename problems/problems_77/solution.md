# [Python] 回溯

> slug: python-hui-su-by-himymben-ghog
> date: 2024-03-10
> tags: C, Go, Java, Python3, TypeScript
> question: Combinations (combinations)
> url: https://leetcode.cn/problems/combinations/solutions/rlebej/python-hui-su-by-himymben-ghog/

---

> Problem: [77. 组合](https://leetcode.cn/problems/combinations/description/)

[TOC]

# 思路

> 回溯

# 解题方法

> n个里选k个，可以有n - k个数依次被跳过


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
  
