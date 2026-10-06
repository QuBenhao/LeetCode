# [Python] Multiplication and addition of congruences

> slug: python-tong-yu-xiang-cheng-xiang-jia-by-tzatt
> date: 2024-03-07
> tags: C, Go, Java, Python3, TypeScript
> question: Find the Divisibility Array of a String (find-the-divisibility-array-of-a-string)
> url: https://leetcode.cn/problems/find-the-divisibility-array-of-a-string/solutions/Yi7g1j/python-tong-yu-xiang-cheng-xiang-jia-by-tzatt/

---

> Problem: [2575. 找出字符串的可整除数组](https://leetcode.cn/problems/find-the-divisibility-array-of-a-string/description/)

[TOC]

# Intuition

> 1 Reflexivity: a ≡ a (mod m)
2 Symmetry: if a ≡ b(mod m), then b ≡ a (mod m)
3 Transitivity: if a ≡ b (mod m) and b ≡ c (mod m), then a ≡ c (mod m)
4 Addition of congruences: if a ≡ b (mod m) and c≡d(mod m), then a+-c≡b+-d (mod m)
5 Multiplication of congruences: if a ≡ b (mod m) and c≡d(mod m), then ac≡bd (mod m)

# Approach

> Starting from the first digit, compute each prefix's remainder using the mathematical properties of congruence.

# Complexity

Time complexity:
> $O(n)$

Space complexity:
> $O(n)$



# Code
```Python3 []
class Solution:
    def divisibilityArray(self, word: str, m: int) -> List[int]:
        ans, cur = [], 0
        for c in word:
            cur = (10 * cur + (ord(c) - ord('0'))) % m
            ans.append(1 if not cur else 0)
        return ans
```
  
