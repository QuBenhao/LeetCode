# [Python] 模拟

> Author: Benhao
> Date: 2022-11-29
> Upvotes: 5
> Tags: Go, Java, JavaScript, Python3, TypeScript

---

> Problem: [1758. 生成交替二进制字符串的最少操作数](https://leetcode.cn/problems/minimum-changes-to-make-alternating-binary-string/description/)

[TOC]

# 思路
> 交替二进制串只有两种，"010101"或者"101010"，我们统计与哪种更接近即可

# 解题方法
> 逐位统计不同的个数，另一个个数恰相反。返回最小的即可

# 复杂度
- 时间复杂度: 
> $O(n)$

- 空间复杂度: 
> $O(1)$

# Code
```Python3 []

class Solution:
    def minOperations(self, s: str) -> int:
        return min(d := sum(int(s[i]) != i & 1 for i in range(len(s))), len(s) - d)
```
