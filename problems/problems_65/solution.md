# [Python] DFA state transitions

> Author: Benhao
> Date: 2021-06-17
> Upvotes: 17
> Tags: Python, Python3

---

### Approach
![DFA.png](https://pic.leetcode.cn/1623892458-ENdUhr-DFA.png)
Image from [solution](https://leetcode.com/problems/valid-number/discuss/23728/A-simple-solution-in-Python-based-on-DFA)

1: Initial state (empty string or only spaces)
2: Sign
3: Digits (such as -164; can be an ending state)
4: Decimal point
5: Digits after the decimal point (such as .721 or -123.6; can be an ending state)
6: Exponent e
7: Sign after the exponent
8: Digits after the exponent (such as +1e-6; can be an ending state)
9: Spaces after states 3,5,8 (mainly to reject strings such as "1 1")

### Code

```python3
class Solution:
    def isNumber(self, s: str) -> bool:
        # DFA transitions: dict[action] -> successor
        states = [{},
                  # state 1
                  {"blank":1,"sign":2,"digit":3,"dot":4},
                  # state 2
                  {"digit":3,"dot":4},
                  # state 3
                  {"digit":3,"dot":5,"e|E":6,"blank":9},
                  # state 4
                  {"digit":5},
                  # state 5
                  {"digit":5,"e|E":6,"blank":9},
                  # state 6
                  {"sign":7,"digit":8},
                  # state 7
                  {"digit":8},
                  # state 8
                  {"digit":8,"blank":9},
                  # state 9
                  {"blank":9}]

        def strToAction(st):
            if '0' <= st <= '9':
                return "digit"
            if st in "+-":
                return "sign"
            if st in "eE":
                return "e|E"
            if st == '.':
                return "dot"
            if st == ' ':
                return "blank"
            return None

        currState = 1
        for c in s:
            action = strToAction(c)
            if action not in states[currState]:
                return False
            currState = states[currState][action]

        # ending states: 3,5,8,9
        return currState in {3,5,8,9}
```
