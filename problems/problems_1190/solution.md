# [Python] 奇思妙想的栈树

> Author: Benhao
> Date: 2021-05-26
> Upvotes: 10
> Tags: Python, Python3

---

### 解题思路
外面的()嵌套里面的()，里面的()就像是外面的()的子节点。本质上和第二段写法一样

### 代码

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

不建Class，直接用[[]]
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