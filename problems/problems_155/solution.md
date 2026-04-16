# [Python] 辅助栈

> Author: Benhao
> Date: 2024-03-16
> Upvotes: 1
> Tags: C, Go, Java, Python3, TypeScript

---


> Problem: [155. 最小栈](https://leetcode.cn/problems/min-stack/description/)

[TOC]

# 思路

> 用辅助栈记录当前元素进栈时的最小元素是什么，方便之后取

# 解题方法

> 辅助栈

# 复杂度

时间复杂度:
> $O(1)$

空间复杂度:
> $O(n)$



# Code
```Python3 []
class MinStack:

    def __init__(self):
        self.stack = []
        self.help = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.help.append(val if not self.help or self.help[-1] > val else self.help[-1])

    def pop(self) -> None:
        self.stack.pop()
        self.help.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.help[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
```
  
