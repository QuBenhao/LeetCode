# [Python] 栈+动态规划

> Author: Benhao
> Date: 2021-06-14
> Upvotes: 2
> Tags: Python, Python3

---

### 解题思路
其实这题就是披着计算器外衣的动态规划。
我们先考虑没有括号，我们有一个最小单元，单纯类似"0&1|0"时我们怎么计算最小的操作数使它相反。
0 | 0， 我们只需要两边的某一个变为1
0 | 1 或者 1 | 0， 我们只需要把符号变成&
1 | 1，我们需要将某一边变成0且符号变成&
0 & 0，我们需要将某一边变为1且符号变为|
0 & 1 或者 1 & 0， 我们只需要将符号变为|
1 & 1, 我们需要将某一边变为0

这个时候我们再引入括号，可以发现类似于计算器，我们要优先计算最底层不受其他计算影响的括号(栈),
我们去掉每个括号的时候，将它简化为它的`结果值,转换最小的操作数`。
我们将简化后的结果加入原来这个括号所属的父节点(括号)中，
不停维护这两个变量即可直到最后即可。

为简化代码，我们将每个单独的0和1也看做一种被括号包裹的最小单元，所以加入时是他们的值和转换需要的操作1。


### 代码

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
        # l中没有括号，计算l的结果:val,change
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