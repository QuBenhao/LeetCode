# [Python] Memoized search

> Author: Benhao
> Date: 2024-03-22
> Upvotes: 2
> Tags: C, Go, Java, Python3, TypeScript

---


> Problem: [97. 交错字符串](https://leetcode.cn/problems/interleaving-string/description/)

[TOC]

# Intuition

> At first, it seemed enough to merge the two sequences in order by advancing two pointers to the end. But s1 and s2 can have the same current character followed by different characters, so the choice affects later steps. Use memoized search: after making a choice, use the result of the remaining search to determine whether it was valid.

# Approach

> Memoized search

# Complexity

Time complexity:
> $O(m + n)$

Space complexity:
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
  
