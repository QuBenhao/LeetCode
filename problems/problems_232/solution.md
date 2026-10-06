# [Python] Simulate a queue with stacks

> Author: Benhao
> Date: 2024-03-04
> Upvotes: 2
> Tags: C, Go, Java, Python3, TypeScript

---


> Problem: [232. 用栈实现队列](https://leetcode.cn/problems/implement-queue-using-stacks/description/)

[TOC]

# Intuition

> To simulate first-in, first-out with last-in, first-out, transfer all elements to a second stack when removing an element. The element that should leave first will then be at the top.

# Approach

> Simulation with two stacks

# Complexity

Time complexity:
> $O(n)$

Space complexity:
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
  
