# [Python] Simulation

> slug: python-mo-ni-by-himymben-1bae
> date: 2024-03-11
> tags: C, Go, Java, Python3, TypeScript
> question: Capitalize the Title (capitalize-the-title)
> url: https://leetcode.cn/problems/capitalize-the-title/solutions/Ueh66a/python-mo-ni-by-himymben-1bae/

---

> Problem: [2129. 将标题首字母大写](https://leetcode.cn/problems/capitalize-the-title/description/)

[TOC]

# Intuition

> Split the string on spaces and check each word's length. As required, either capitalize the first letter and lowercase the rest, or lowercase the whole word.

# Approach

> Simulation

# Complexity

Time complexity:
> $O(n)$

Space complexity:
> $O(n)$



# Code
```Python3 []
class Solution:
    def capitalizeTitle(self, title: str) -> str:
        return " ".join([s.capitalize() if len(s) > 2 else s.lower() for s in title.split(" ")])
```
  
