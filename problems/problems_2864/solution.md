# [Python] Greedy

> slug: python-tan-xin-by-himymben-kikb
> date: 2024-03-13
> tags: C, Go, Java, Python3, TypeScript
> question: Maximum Odd Binary Number (maximum-odd-binary-number)
> url: https://leetcode.cn/problems/maximum-odd-binary-number/solutions/PBxoLs/python-tan-xin-by-himymben-kikb/

---

> Problem: [2864. 最大二进制奇数](https://leetcode.cn/problems/maximum-odd-binary-number/description/)

[TOC]

# Intuition

> An odd binary number must end in 1. To maximize it, place the remaining 1s on the left and the 0s on the right.

# Approach

> Count the 1s and construct the result greedily.

# Complexity

Time complexity:
> $O(n)$

Space complexity:
> $O(n)$



# Code
```Python3 []
class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        return "1" * (ones - 1) + "0" * (len(s) - ones) + "1" if (ones := s.count("1")) else ""
```
  
