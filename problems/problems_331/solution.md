# [Python] Stack or counting

> Author: Benhao
> Date: 2021-03-12
> Upvotes: 1
> Tags: C, Go, Java, Python3, TypeScript

---

### Approach
Use a stack to simulate removing completed nodes.

Alternatively, count available slots to validate the serialization. The tree initially has one slot.
Start with the root slot, total = 1. A number consumes one slot and creates two, while '#' consumes one slot. If slots reach 0 while nodes remain, return False. All slots should be filled at the end, leaving 0.

### Code

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
