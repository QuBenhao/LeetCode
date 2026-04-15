# 模拟

> Author: Benhao
> Date: 2022-12-15
> Upvotes: 1
> Tags: Go, Java, JavaScript, Python3, TypeScript

---

> Problem: [1945. 字符串转化后的各位数字之和](https://leetcode.cn/problems/sum-of-digits-of-string-after-convert/description/)

[TOC]

# 思路
> 按题意模拟

# 解题方法
> 循环统计数变为多少 (字符串偷懒)

# Code
```Python3 []

class Solution:
    def getLucky(self, s: str, k: int) -> int:
        s = "".join(str(ord(c) - ord('a') + 1) for c in s)
        for _ in range(k):
            s = str(sum(ord(c) - ord('0') for c in s))
        return int(s)
```
