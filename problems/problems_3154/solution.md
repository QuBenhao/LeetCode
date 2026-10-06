# [Python] Memoized search

> Author: Benhao
> Date: 2024-08-19
> Upvotes: 1
> Tags: Memoization, Python3

---


> Problem: [3154. 到达第 K 级台阶的方案数](https://leetcode.cn/problems/find-number-of-ways-to-reach-the-k-th-stair/description/)

[TOC]

# Intuition

> Track the current position and jump, then recursively count the ways to reach k

# Solution steps

> Use a negative number to record that the previous operation was -1, eliminating one state variable

# Code
```Python3 []
class Solution:

    def waysToReachStair(self, k: int) -> int:
        @lru_cache(None)
        def dfs(cur: int, jump: int) -> int:
            ans = 0
            if abs(cur) == k:
                ans += 1
            elif cur > k + 1 or cur < -k:
                return 0
            if cur > 0:
                ans += dfs(-cur + 1, jump)
            ans += dfs(abs(cur) + (1 << jump), jump + 1)
            return ans

        return dfs(1, 0)
```
  
