# [Python] Backtracking

> Author: Benhao
> Date: 2024-03-11
> Upvotes: 2
> Tags: C, Go, Java, Python3, TypeScript

---


> Problem: [39. 组合总和](https://leetcode.cn/problems/combination-sum/description/)

[TOC]

# Intuition

> Backtracking

# Approach

> Enumerate whether to select the current element. If skipped, it cannot be selected later. If selected, continue recursively checking the sum.

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
            # Skip the current element
            dfs(x - 1, s)
            # Select the current element
            path.append(candidates[x])
            dfs(x, s - candidates[x])
            path.pop()
        
        dfs(len(candidates) - 1, target)
        return ans
```
  
