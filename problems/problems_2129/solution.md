# [Python] 模拟

> slug: python-mo-ni-by-himymben-1bae
> date: 2024-03-11
> tags: C, Go, Java, Python3, TypeScript
> question: Capitalize the Title (capitalize-the-title)
> url: https://leetcode.cn/problems/capitalize-the-title/solutions/Ueh66a/python-mo-ni-by-himymben-1bae/

---

> Problem: [2129. 将标题首字母大写](https://leetcode.cn/problems/capitalize-the-title/description/)

[TOC]

# 思路

> 按空格拆分字符串，判断每个字符串长度，按要求首字母大写其余小写，或者小写

# 解题方法

> 模拟

# 复杂度

时间复杂度:
> $O(n)$

空间复杂度:
> $O(n)$



# Code
```Python3 []
class Solution:
    def capitalizeTitle(self, title: str) -> str:
        return " ".join([s.capitalize() if len(s) > 2 else s.lower() for s in title.split(" ")])
```
  
