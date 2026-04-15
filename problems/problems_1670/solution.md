# [Python] 使用两个双端队列保持平衡

> Author: Benhao
> Date: 2021-05-26
> Upvotes: 0
> Tags: Python, Python3

---

### 解题思路
通过分别存储前半和后半且维护他们的长度差，保证中间的插入位置总是front的最后。
而中间出的时候在front的最后后者back的最前，看两者的长度。

### 代码

```python3
class FrontMiddleBackQueue:

    def __init__(self):
        self.front = deque([])
        self.back = deque([])


    def pushFront(self, val: int) -> None:
        self.front.appendleft(val)
        self.balance()

    def pushMiddle(self, val: int) -> None:
        self.front.append(val)
        self.balance()

    def pushBack(self, val: int) -> None:
        self.back.append(val)
        self.balance()

    def popFront(self) -> int:
        if not self.front and not self.back:
            return -1
        if self.front:
            val = self.front.popleft()
        else:
            val = self.back.popleft()
        self.balance()
        return val

    def popMiddle(self) -> int:
        if not self.front and not self.back:
            return -1
        if len(self.front) >= len(self.back):
            val = self.front.pop()
        else:
            val = self.back.popleft()
        self.balance()
        return val

    def popBack(self) -> int:
        if not self.front and not self.back:
            return -1
        if self.back:
            val = self.back.pop()
        else:
            val = self.front.pop()
        self.balance()
        return val
    
    def balance(self):
        while len(self.back) > len(self.front) + 1:
            self.front.append(self.back.popleft())
        while len(self.front) > len(self.back):
            self.back.appendleft(self.front.pop())


# Your FrontMiddleBackQueue object will be instantiated and called as such:
# obj = FrontMiddleBackQueue()
# obj.pushFront(val)
# obj.pushMiddle(val)
# obj.pushBack(val)
# param_4 = obj.popFront()
# param_5 = obj.popMiddle()
# param_6 = obj.popBack()
```