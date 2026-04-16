# [Python] 记忆化搜索

> Author: Benhao
> Date: 2024-03-22
> Upvotes: 2
> Tags: C, Go, Java, Python3, TypeScript

---


> Problem: [97. 交错字符串](https://leetcode.cn/problems/interleaving-string/description/)

[TOC]

# 思路

> 一开始以为将两个序列按序排就好，双指针往后走完。后面一想不对，s1和s2可以是一样的字符，但后面跟的不一样的字符，每次选谁是对后面有影响的。所以采用记忆化搜索，在做出选择后根据后面的结果判断当前的选择是否正确

# 解题方法

> 记忆化搜索

# 复杂度

时间复杂度:
> $O(m + n)$

空间复杂度:
> $O(m + n)$



# Code
```Python3 []
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        len1, len2 = len(s1), len(s2)
        if len1 + len2 != len(s3):
            return False

        @lru_cache(None)
        def dfs(idx1, idx2):
            return True if idx1 == len1 and idx2 == len2 \
                else ((idx1 < len1 and s1[idx1] == s3[idx1 + idx2] and dfs(idx1 + 1, idx2))
                      or (idx2 < len2 and s2[idx2] == s3[idx1 + idx2] and dfs(idx1, idx2 + 1)))

        return dfs(0, 0)
```
  
