# [Python] 回溯

> Author: Benhao
> Date: 2024-03-11
> Upvotes: 2
> Tags: C, Go, Java, Python3, TypeScript

---


> Problem: [39. 组合总和](https://leetcode.cn/problems/combination-sum/description/)

[TOC]

# 思路

> 回溯

# 解题方法

> 枚举选不选当前，不选的话以后都不能再选了，选的话递归继续判断和

# Code
```Python3 []
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []
        path = []

        def dfs(x, s):
            if s == 0:
                ans.append(list(path))
                return
            if x < 0 or s < 0:
                return
            # 不选当前
            dfs(x - 1, s)
            # 选当前
            path.append(candidates[x])
            dfs(x, s - candidates[x])
            path.pop()
        
        dfs(len(candidates) - 1, target)
        return ans
```
  
