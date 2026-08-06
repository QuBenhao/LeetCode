# [Python] 模拟

> slug: python-mo-ni-by-himymben-drwh
> date: 2024-03-10
> tags: C, Go, Java, Python3, TypeScript
> question: Bulls and Cows (bulls-and-cows)
> url: https://leetcode.cn/problems/bulls-and-cows/solutions/Juwb29/python-mo-ni-by-himymben-drwh/

---

> Problem: [299. 猜数字游戏](https://leetcode.cn/problems/bulls-and-cows/description/)

[TOC]

# 思路

> 模拟

# 解题方法

> 统计每个数字的个数，统计一样位置的数目A，一样数字不一样位置的数目B由两者一样数字的数目减去A得到

# 复杂度

时间复杂度:
> $O(n)$

空间复杂度:
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
  
