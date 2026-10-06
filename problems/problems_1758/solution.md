# [Python] Simulation

> Author: Benhao
> Date: 2022-11-29
> Upvotes: 5
> Tags: Go, Java, JavaScript, Python3, TypeScript

---

> Problem: [1758. 生成交替二进制字符串的最少操作数](https://leetcode.cn/problems/minimum-changes-to-make-alternating-binary-string/description/)

[TOC]

# Intuition
> There are only two alternating binary patterns, "010101" and "101010". Find which one is closer.

# Approach
> Count mismatching positions. The other pattern has the complementary count; return the smaller count.

# Complexity
- Time complexity:
> $O(n)$

- Space complexity:
> $O(1)$

# Code
```Python3 []

class Solution:
    def minOperations(self, s: str) -> int:
        return min(d := sum(int(s[i]) != i & 1 for i in range(len(s))), len(s) - d)
```
