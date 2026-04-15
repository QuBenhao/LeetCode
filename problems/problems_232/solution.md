# [Python] 栈模拟队列

> Author: Benhao
> Date: 2024-03-04
> Upvotes: 2
> Tags: C, Go, Java, Python3, TypeScript

---


> Problem: [232. 用栈实现队列](https://leetcode.cn/problems/implement-queue-using-stacks/description/)

[TOC]

# 思路

> 先进后出模拟先进先出的话，只需要在出的时候用另一个栈将所有栈内元素退出来放到另一个栈，这样要先出的元素就会在栈顶

# 解题方法

> 双栈模拟

# 复杂度

时间复杂度:
> $O(n)$

空间复杂度:
> $O(n)$



# Code
```Python3 []
class MyQueue:

    def __init__(self):
        self.stack = []
        self.reverse = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        if not self.reverse:
            while self.stack:
                self.reverse.append(self.stack.pop())
        return self.reverse.pop()

    def peek(self) -> int:
        return self.reverse[-1] if self.reverse else self.stack[0]

    def empty(self) -> bool:
        return len(self.stack) == 0 and len(self.reverse) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
```
  
