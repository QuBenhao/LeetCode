# [Python] 栈

> Author: Benhao
> Date: 2024-03-07
> Upvotes: 1
> Tags: C, Go, Java, Python3, TypeScript

---


> Problem: [71. 简化路径](https://leetcode.cn/problems/simplify-path/description/)

[TOC]

# 思路

> 以栈去处理".."的弹出上一层

# 解题方法

> 按层级"/"分割，以栈处理中间的路径变化，最后再以"/"组合

# 复杂度

时间复杂度:
> $O(n)$

空间复杂度:
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
  
