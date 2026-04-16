# [Python] 统计字符数目一致

> Author: Benhao
> Date: 2024-03-27
> Upvotes: 0
> Tags: C, Go, Java, Python3, TypeScript

---


> Problem: [242. 有效的字母异位词](https://leetcode.cn/problems/valid-anagram/description/)

[TOC]

# 思路

> 统计各字符数目一致即可

# 解题方法

> 模拟

# 复杂度

时间复杂度:
> $O(n)$

空间复杂度:
> $O(n)$



# Code
```Python3 []
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return len(s) == len(t) and Counter(s) == Counter(t)
```
  
