# [Python] 栈 or 计数

> Author: Benhao
> Date: 2021-03-12
> Upvotes: 1
> Tags: C, Go, Java, Python3, TypeScript

---

### 解题思路
用栈模拟节点消除过程。

或者计数统计是否合法，初始树只有一个槽位，
初始root位，total = 1，遇到数字槽位会减1再加2，遇到'#'槽位会减1。如果某一时刻槽位为0，但仍有node没填，return False。最终槽位应该被填满，为0。

### 代码

```Python3 []
class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        splits = preorder.split(",")
        stack = []
        for node in splits:
            stack.append(node)
            while len(stack) >= 3 and stack[-1] == "#" and stack[-2] == "#" and stack[-3] != "#":
                for _ in range(3):
                    stack.pop()
                stack.append("#")
        return len(stack) == 1 and stack[0] == "#"
```
```Python3 []
class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        total = 1
        for node in preorder.split(","):
            total -= 1
            if total < 0:
                return False
            if node != "#":
                total += 2
        return total == 0
```