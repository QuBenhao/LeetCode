# [Python] Stack

> Author: Benhao
> Date: 2024-03-07
> Upvotes: 1
> Tags: C, Go, Java, Python3, TypeScript

---


> Problem: [71. 简化路径](https://leetcode.cn/problems/simplify-path/description/)

[TOC]

# Intuition

> Use a stack to pop the previous level for "..".

# Approach

> Split levels on "/", use a stack to handle path changes, then join the result with "/".

# Complexity

Time complexity:
> $O(n)$

Space complexity:
> $O(n)$



# Code
```Python3 []
class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        for p in path.split("/"):
            if p == ".." and stack:
                stack.pop()
            elif p not in "..":
                stack.append(p)
        return "/" + "/".join(stack)
```
  
