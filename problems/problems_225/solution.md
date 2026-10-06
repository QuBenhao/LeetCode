# [Python] Simulation

> Author: Benhao
> Date: 2024-03-03
> Upvotes: 1
> Tags: C, Go, Java, Python3, TypeScript

---


> Problem: [225. 用队列实现栈](https://leetcode.cn/problems/implement-stack-using-queues/description/)

[TOC]

# Intuition

> Simulate a stack with a queue

# Approach

> The key is how to remove the last element. Dequeue the preceding elements and enqueue them again, bringing the last element to the front for removal.

# Complexity

Time complexity:
> $O(n)$

Space complexity:
> $O(n)$



# Code
```Python3 []
class MyStack:

    def __init__(self):
        self.queue = deque([])

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        for _ in range(len(self.queue) - 1):
            self.queue.append(self.queue.popleft())
        return self.queue.popleft()

    def top(self) -> int:
        return self.queue[-1]

    def empty(self) -> bool:
        return len(self.queue) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
```
  
