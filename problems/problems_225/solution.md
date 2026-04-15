# [Python] 模拟

> Author: Benhao
> Date: 2024-03-03
> Upvotes: 1
> Tags: C, Go, Java, Python3, TypeScript

---


> Problem: [225. 用队列实现栈](https://leetcode.cn/problems/implement-stack-using-queues/description/)

[TOC]

# 思路

> 用队列模拟栈

# 解题方法

> 关键点在于怎么弹出最后一个元素。我们可以按队列的特性将队列前面的重新弹出进入一次，这样就可以取出最后一个了

# 复杂度

时间复杂度:
> $O(n)$

空间复杂度:
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
  
