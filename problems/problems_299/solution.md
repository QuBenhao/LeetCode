# [Python] Simulation

> slug: python-mo-ni-by-himymben-drwh
> date: 2024-03-10
> tags: C, Go, Java, Python3, TypeScript
> question: Bulls and Cows (bulls-and-cows)
> url: https://leetcode.cn/problems/bulls-and-cows/solutions/Juwb29/python-mo-ni-by-himymben-drwh/

---

> Problem: [299. 猜数字游戏](https://leetcode.cn/problems/bulls-and-cows/description/)

[TOC]

# Intuition

> Simulation

# Approach

> Count each digit and count matching positions as A. The number B of matching digits in different positions is the total shared digit count minus A.

# Complexity

Time complexity:
> $O(n)$

Space complexity:
> $O(n)$



# Code
```Python3 []
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        cs, cg = Counter(secret), Counter(guess)
        a = sum(1 if chars == charg else 0 for chars, charg in zip(secret, guess))
        b = sum(min(cs[str(i)], cg[str(i)]) for i in range(10)) - a
        return f"{a}A{b}B"
```
  
