# [Python] 贪心

> slug: python-tan-xin-by-himymben-kikb
> date: 2024-03-13
> tags: C, Go, Java, Python3, TypeScript
> question: Maximum Odd Binary Number (maximum-odd-binary-number)
> url: https://leetcode.cn/problems/maximum-odd-binary-number/solutions/PBxoLs/python-tan-xin-by-himymben-kikb/

---

> Problem: [2864. 最大二进制奇数](https://leetcode.cn/problems/maximum-odd-binary-number/description/)

[TOC]

# 思路

> 二进制的奇数最后一位必须是1，最大的话就是把所有的1都往左边放，0往右边放

# 解题方法

> 统计1的个数，贪心构造即可

# 复杂度

时间复杂度:
> $O(n)$

空间复杂度:
> $O(n)$



# Code
```Python3 []
class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        return "1" * (ones - 1) + "0" * (len(s) - ones) + "1" if (ones := s.count("1")) else ""
```
  
