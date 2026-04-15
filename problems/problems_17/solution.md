# [Python] product

> Author: Benhao
> Date: 2024-03-02
> Upvotes: 1
> Tags: C, Go, Java, Python3, TypeScript

---


> Problem: [17. 电话号码的字母组合](https://leetcode.cn/problems/letter-combinations-of-a-phone-number/description/)

[TOC]

# 思路

> 枚举组合

# 解题方法

> 使用itertools


# Code
```Python3 []
MAPS = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        return ["".join(p) for p in product(*[list(MAPS[c]) for c in digits])] if digits else []
```
  
