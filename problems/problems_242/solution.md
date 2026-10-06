# [Python] Compare character counts

> Author: Benhao
> Date: 2024-03-27
> Upvotes: 0
> Tags: C, Go, Java, Python3, TypeScript

---


> Problem: [242. 有效的字母异位词](https://leetcode.cn/problems/valid-anagram/description/)

[TOC]

# Intuition

> Check that the counts of each character match.

# Approach

> Simulation

# Complexity

Time complexity:
> $O(n)$

Space complexity:
> $O(n)$



# Code
```Python3 []
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return len(s) == len(t) and Counter(s) == Counter(t)
```
  
