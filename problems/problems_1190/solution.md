# [Python] An imaginative stack tree

> Author: Benhao
> Date: 2021-05-26
> Upvotes: 10
> Tags: Python, Python3

---

### Approach
Outer () contain inner (), so the inner () act like child nodes of the outer (). This is essentially the same as the second implementation.

### Code

```python3
class Solution:
    def reverseParentheses(self, s: str) -> str:
        ans = []
        node = None
        for c in s:
            if c == '(':
                if node is None:
                    node = StackTree(None)
                else:
                    node = StackTree(node)
            elif c == ')':
                if node.parent is not None:
                    while node.root:
                        node.parent.root.append(node.root.pop())
                    node = node.parent
                else:
                    while node.root:
                        ans.append(node.root.pop())
                    node = None
            else:
                if node is None:
                    ans.append(c)
                else:
                    node.root.append(c)
        return "".join(ans)


class StackTree:
    def __init__(self, parent):
        self.root = []
        self.parent = parent

```

Use [[]] directly without defining a Class
```python3
class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = [[]]
        for c in s:
            if c == '(':
                stack.append([])
            elif c == ')':
                temp = reversed(stack.pop())
                stack[-1] += temp
            else:
                stack[-1].append(c)
        return "".join(stack[0])
```
