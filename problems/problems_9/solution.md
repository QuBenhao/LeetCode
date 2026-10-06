# [Python] Simulation

> slug: python-mo-ni-by-himymben-n9ew
> date: 2024-03-04
> tags: C, Go, Java, Python3, TypeScript
> question: Palindrome Number (palindrome-number)
> url: https://leetcode.cn/problems/palindrome-number/solutions/gVEmw7/python-mo-ni-by-himymben-n9ew/

---

> Problem: [9. 回文数](https://leetcode.cn/problems/palindrome-number/description/)

[TOC]

# Intuition

> The basic palindrome check is whether the reversed second half matches the first half.

# Approach

> Repeated division extracts digits from back to front. When the value is less than or equal to the original number, we have processed at least half of it.
For an odd number of digits, compare the two values after accounting for a factor of ten. For an even number of digits, check whether they are equal.

# Complexity

Time complexity:
> $O(n)$

Space complexity:
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
  
