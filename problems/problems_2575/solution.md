# [Python] 同余相乘相加

> slug: python-tong-yu-xiang-cheng-xiang-jia-by-tzatt
> date: 2024-03-07
> tags: C, Go, Java, Python3, TypeScript
> question: Find the Divisibility Array of a String (find-the-divisibility-array-of-a-string)
> url: https://leetcode.cn/problems/find-the-divisibility-array-of-a-string/solutions/Yi7g1j/python-tong-yu-xiang-cheng-xiang-jia-by-tzatt/

---

> Problem: [2575. 找出字符串的可整除数组](https://leetcode.cn/problems/find-the-divisibility-array-of-a-string/description/)

[TOC]

# 思路

> 1 反身性 a ≡ a (mod m)
2 对称性 若a ≡ b(mod m) 则b ≡ a (mod m)
3 传递性 若a ≡ b (mod m)，b ≡ c (mod m),则a ≡ c (mod m)
4 同余式相加若a ≡ b (mod m)，c≡d(mod m)，则a+-c≡b+-d（mod m）
5 同余式相乘 若a ≡ b (mod m)，c≡d(mod m)，则ac≡bd（mod m）

# 解题方法

> 从首位开始依次计算每一位的余即可，掌握同余性质的数学原理

# 复杂度

时间复杂度:
> $O(n)$

空间复杂度:
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
  
