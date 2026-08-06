# [Python] 模拟

> slug: python-mo-ni-by-himymben-n9ew
> date: 2024-03-04
> tags: C, Go, Java, Python3, TypeScript
> question: Palindrome Number (palindrome-number)
> url: https://leetcode.cn/problems/palindrome-number/solutions/gVEmw7/python-mo-ni-by-himymben-n9ew/

---

> Problem: [9. 回文数](https://leetcode.cn/problems/palindrome-number/description/)

[TOC]

# 思路

> 判断回文的基本思路是后半段的反转与前半段一致

# 解题方法

> 数字我们可以通过辗转相除从后往前取数字，当小于等于原数时，说明我们已经处理过半了
如果原数字是奇数长度，则两者判断十倍差异。如果原数字是偶数长度，则判断两者是否一致。

# 复杂度

时间复杂度:
> $O(n)$

空间复杂度:
> $O(1)$



# Code
```Python3 []
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (not x % 10 and x):
            return False
        reverse = 0
        while x > reverse:
            reverse = 10 * reverse + x % 10
            x //= 10
        return x == reverse or reverse // 10 == x
```
  
