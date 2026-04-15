# [Python] 双向BFS(100%) A*见评论

> Author: Benhao
> Date: 2021-06-24
> Upvotes: 16
> Tags: Python, Python3

---

### 解题思路
双向BFS的讲解见[三叶的如何使用「双向 BFS」解决搜索空间爆炸问题](https://leetcode.cn/problems/word-ladder/solution/gong-shui-san-xie-ru-he-shi-yong-shuang-magjd/)

### 代码

```python3
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        class Queue:
            def __init__(self):
                self.queue = deque([])
                self.explored = dict()

            def __contains__(self, item):
                return item in self.explored

            def __len__(self):
                return len(self.queue)

            def add(self, other):
                self.queue.append(other[1])
                self.explored[other[1]] = other[0]

            def pop(self):
                return self.queue.popleft()
        
        def action(string):
            nxt = []
            for i,c in enumerate(string):
                nxt.append(string[:i] + str((int(c) + 1) % 10) + string[i+1:])
                nxt.append(string[:i] + str((int(c) - 1) % 10) + string[i+1:])
            return nxt

        init = "0000"
        if target == init:
            return 0
        elif init in deadends:
            return -1
    
        deadends = set(deadends)
        front, back = Queue(), Queue()
        front.add((0, init))
        back.add((1, target))
        while front and back:
            if len(front) > len(back):
                ts, ot = back, front
            else:
                ts, ot = front, back
            for _ in range(len(ts)):
                s = ts.pop()
                for successor in action(s):
                    if successor not in ts and successor not in deadends:
                        if successor in ot:
                            return ts.explored[s] + ot.explored[successor]
                        ts.add((ts.explored[s] + 1, successor))
        return -1
```
通用模板，只需要更改action和update里面的constraint(比如可能是in而不是not int)
```python3
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        class Queue:
            def __init__(self):
                self.queue = deque([])
                self.cost = dict()

            def __contains__(self, item):
                return item in self.cost

            def __len__(self):
                return len(self.queue)

            def add(self, item):
                self.queue.append(item[1])
                self.cost[item[1]] = item[0]

            def pop(self):
                return self.queue.popleft()

            # update function
            def update(self, other, constraint=None):
                for _ in range(len(self.queue)):
                    s = self.pop()
                    cost = self.cost[s]
                    for successor in action(s):
                        if successor not in self and (not constraint or successor not in constraint):
                            if successor in other:
                                return cost + other.cost[successor]
                            self.add((cost + 1, successor))
                return -1

        # transition function
        def action(string):
            return [string[:i] + str((int(c) + d) % 10) + string[i + 1:] for d in (-1, 1) for i, c in enumerate(string)]

        init = "0000"
        if target == init:
            return 0
        deadends = set(deadends)
        if init in deadends:
            return -1
        front, back = Queue(), Queue()
        front.add((0, init))
        back.add((1, target))
        while front and back:
            if len(front) > len(back):
                res = back.update(front, deadends)
            else:
                res = front.update(back, deadends)
            if res != -1:
                return res
        return -1
```