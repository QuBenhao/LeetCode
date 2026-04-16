# [Python] 栈

> Author: Benhao
> Date: 2024-03-01
> Upvotes: 2
> Tags: C, Go, Java, Python3, TypeScript

---


> Problem: [20. 有效的括号](https://leetcode.cn/problems/valid-parentheses/description/)

[TOC]

# 思路

> 遇见这种左右括号对称消除的，直接选择栈就行，因为最新的右括号必须消除的是最后一个左括号，这符合栈的概念

# 解题方法

> 应用栈

# 复杂度

时间复杂度:
> $O(n)$

空间复杂度:
> $O(n)$



# Code
```Python3 []
LEFT, RIGHT = "({[", ")}]"
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in RIGHT:
                if not stack or stack[-1] not in LEFT or LEFT.index(stack[-1]) != RIGHT.index(c):
                    return False
                stack.pop()
            else:
                stack.append(c)
        return not stack
```
  
