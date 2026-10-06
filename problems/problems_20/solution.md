# [Python] Stack

> Author: Benhao
> Date: 2024-03-01
> Upvotes: 2
> Tags: C, Go, Java, Python3, TypeScript

---


> Problem: [20. 有效的括号](https://leetcode.cn/problems/valid-parentheses/description/)

[TOC]

# Intuition

> A stack fits this kind of matching and canceling of opening and closing brackets: the newest closing bracket must cancel the most recent opening bracket.

# Approach

> Use a stack

# Complexity

Time complexity:
> $O(n)$

Space complexity:
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
  
