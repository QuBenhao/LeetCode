# [Python] 凑9游戏

> Author: Benhao
> Date: 2021-07-11
> Upvotes: 2
> Tags: Python, Python3

---

### 解题思路
Bob能在对手干扰下赢的策略只有保证始终能凑出9，只有本身的差距是9的倍数而且两边操作数足够凑出这个差距。

### 代码

```python
class Solution(object):
    def sumGame(self, num):
        """
        :type num: str
        :rtype: bool
        """
        s = a = b = 0
        n = len(num)
        for i,c in enumerate(num):
            if i < n // 2:
                if c == '?':
                    a += 1
                else:
                    s += int(c)
            else:
                if c == '?':
                    b += 1
                else:
                    s -= int(c)
        # Alice 先手， 总能使得和不为9的倍数，从而最终的和不相等
        if (a + b) % 2 == 1:
            return True
        # 两人有相同的次数，差为总能凑数9的倍数的话，Bob胜
        if s % 9 == 0 and s // 9 == b - a >> 1:
            return False
        return True
```