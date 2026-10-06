# [Python] Stack + dynamic programming

> Author: Benhao
> Date: 2021-06-14
> Upvotes: 2
> Tags: Python, Python3

---

### Approach
This is dynamic programming disguised as a calculator problem.
First ignore parentheses and consider a small expression such as "0&1|0". How many operations are needed to flip its result?
0 | 0: change either operand to 1.
0 | 1 or 1 | 0: change the operator to &.
1 | 1: change one operand to 0 and the operator to &.
0 & 0: change one operand to 1 and the operator to |.
0 & 1 or 1 & 0: change the operator to |.
1 & 1: change either operand to 0.

With parentheses, use a stack as in a calculator to evaluate the innermost groups first.
Replace each parenthesized group with its `result and minimum operations to flip it`.
Add that simplified result to its parent group.
Maintain these two values until the entire expression has been processed.

To simplify the code, treat each individual 0 or 1 as a minimal group, storing its value and a flip cost of 1.


### Code

```python3
class Solution:
    def minOperationsToFlip(self, expression: str) -> int:
        """
        p1  op  p2  val, change
        0   |   0   0, min(c1,c2)
        0   |   1   1, 1
        1   |   0   1, 1
        1   |   1   1, min(c1,c2)+1
        0   &   0   0, min(c1,c2)+1
        0   &   1   0, 1
        1   &   0   0, 1
        1   &   1   1, min(c1,c2)
        """
        # l contains no parentheses; compute its result as val,change
        def cal(l):
            val, change = l[0]
            idx = 1
            while idx < len(l):
                op = l[idx]
                v, c = l[idx+1]
                if op == '|':
                    if val + v == 1:
                        val, change = 1, 1
                    elif not v:
                        val, change = 0, min(change, c)
                    else:
                        val, change = 1, min(change, c) + 1
                else:
                    if val + v == 1:
                        val, change = 0, 1
                    elif not v:
                        val, change = 0, min(change, c) + 1
                    else:
                        val, change = 1, min(change, c)
                idx += 2
            return val, change

        stack = [[]]
        for c in expression:
            if c == '(':
                stack.append([])
            elif c == ')':
                value, changes = cal(stack.pop())
                stack[-1].append((value,changes))
            elif c in '&|':
                stack[-1].append(c)
            else:
                # val, change for 0 or 1
                stack[-1].append((int(c),1))
        return cal(stack[0])[1]
```
