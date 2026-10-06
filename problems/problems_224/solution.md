# [Python] Two different stack-based approaches

> Author: Benhao
> Date: 2021-03-10
> Upvotes: 1
> Tags: Python

---

### Approach
Approach 1: Store all information in a stack and evaluate at ')' or the end.
Approach 2: Evaluate as you go, using a stack to save intermediate results at parentheses for later evaluation. (See the code comments for details.)

### Code

```python
class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        def perform_cal():
            t = 0
            while stack and len(stack) > 1:
                num = stack.pop()
                op = stack.pop()
                if op == '+':
                    t += num
                elif op == '-':
                    t -= num
                elif op == '(':
                    t += num
                    break
            if len(stack) == 1 and stack[0] != '(':
                o = stack.pop()
                if o == '-':
                    t *= -1
                elif o != '+':
                    t += o
            stack.append(t)

        stack = []
        last_num = None
        for c in s:
            if '0' <= c <= '9':
                if last_num is not None:
                    last_num *= 10
                    last_num += int(c)
                else:
                    last_num = int(c)
            else:
                if last_num is not None:
                    stack.append(last_num)
                    last_num = None
                if c == ')':
                    perform_cal()
                elif c != ' ':
                    stack.append(c)
        if last_num is not None:
            stack.append(last_num)
        perform_cal()
        return stack[0]
```

### Approach 2: Lower time and space complexity

```python
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        cal, num, sign, stack = 0, 0, 1, []
        for c in s:
            if '0' <= c <= '9':
                # to calculate numbers greater than 9, e.g. 123
                num = 10 * num + int(c)
            elif c == '+' or c == '-':
                # when we encounter a '+' or '-', we should calculate the result before this char
                cal += sign * num
                # and reset sign and num
                sign = 1 if c == '+' else -1
                num = 0
            elif c == '(':
                # we are going to calculate result inside '()', store the result first
                stack.append(cal)
                # are we add the result of '()' or minus?
                stack.append(sign)
                # then reset result and sign
                cal, sign = 0, 1
            elif c == ')':
                # we get to the end of '()', we have to add up the results
                cal += sign * num
                # sign
                cal *= stack.pop()
                # result before
                cal += stack.pop()
                # don't need to reset sign here as we will meet '+' or '-' first if any
                num = 0
        cal += sign * num
        return cal
```
