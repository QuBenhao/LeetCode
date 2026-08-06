# [Python] 正反哈希表映射

> slug: python-zheng-fan-ha-xi-biao-ying-she-by-0si7q
> date: 2024-03-07
> tags: C, Go, Java, Python3, TypeScript
> question: Isomorphic Strings (isomorphic-strings)
> url: https://leetcode.cn/problems/isomorphic-strings/solutions/uboW2k/python-zheng-fan-ha-xi-biao-ying-she-by-0si7q/

---

> Problem: [205. 同构字符串](https://leetcode.cn/problems/isomorphic-strings/description/)

[TOC]

# 思路

> 从s的字符映射到t的字符，同时从t的字符映射到s的字符

# 解题方法

> 如果出现对不齐的情况，就无法转化

# 复杂度

时间复杂度:
> $O(n)$

空间复杂度:
> $O(n)$



# Code
```Python3 []
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mp1, mp2 = {}, {}
        for a, b in zip(s, t):
            if a in mp1 and mp1[a] != b:
                return False
            if b in mp2 and mp2[b] != a:
                return False
            mp1[a] = b
            mp2[b] = a
        return True
```
  
