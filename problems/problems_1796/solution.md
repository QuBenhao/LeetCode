# 标题儿

> Author: Benhao
> Date: 2022-12-03
> Upvotes: 15
> Tags: Go, Java, JavaScript, Python3, TypeScript

---

> Problem: [1796. 字符串中第二大的数字](https://leetcode.cn/problems/second-largest-digit-in-a-string/description/)

[TOC]

# 思路
> 模拟遍历统计即可

# 解题方法
> 遍历统计第二大

# 复杂度
- 时间复杂度: 
> $O(n)$

- 空间复杂度: 
> $O(1)$

# Code
```Python3 []

class Solution:
    def secondHighest(self, s: str) -> int:
        m1 = m2 = -1
        for c in s:
            if c.isdigit():
                if (d := int(c)) > m1:
                    m1, m2 = d, m1
                elif d < m1 and d > m2:
                    m2 = d
        return m2

```
