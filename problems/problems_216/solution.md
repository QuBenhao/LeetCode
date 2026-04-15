# [Python] 简单回溯

> Author: Benhao
> Date: 2024-04-21
> Upvotes: 1
> Tags: C, Go, Java, Python3, TypeScript

---


> Problem: [216. 组合总和 III](https://leetcode.cn/problems/combination-sum-iii/description/)

[TOC]

# Code
```Python3 []
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []

        def dfs(path, cur, remain, picks):
            if remain == 0 and not picks:
                ans.append(list(path))
                return
            if not picks or not cur:
                return
            for num in range(min(cur, remain), 0, -1):
                path.append(num)
                dfs(path, num - 1, remain - num, picks - 1)
                path.pop()

        dfs([], 9, n, k)
        return ans
```
  
