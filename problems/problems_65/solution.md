# [Python] DFA 状态机转换

> Author: Benhao
> Date: 2021-06-17
> Upvotes: 17
> Tags: Python, Python3

---

### 解题思路
![DFA.png](https://pic.leetcode.cn/1623892458-ENdUhr-DFA.png)
图片来自[solution](https://leetcode.com/problems/valid-number/discuss/23728/A-simple-solution-in-Python-based-on-DFA)

1:初始状态 (空字符串或者纯空格)
2:符号位
3:数字位 (形如-164,可以作为结束)
4:小数点
5:小数点后的数字(形如.721或者-123.6,可以作为结束)
6:指数e
7:指数后面的符号位
8:指数后面的数字(形如+1e-6,可以作为结束)
9:状态3,5,8后面多了空格(主要为了判断"1 1"是不合理的)

### 代码

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