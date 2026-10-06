# [Python] Index hash map + binary search

> Author: Benhao
> Date: 2022-11-16
> Upvotes: 8
> Tags: Go, Java, JavaScript, Python3, TypeScript

---

> Problem: [792. 匹配子序列的单词数](https://leetcode.cn/problems/number-of-matching-subsequences/description/)

[TOC]

# Intuition
> Map each character to an array of its indices in the string. For each word, repeatedly binary search for the next character's index farther to the right to determine whether it is a subsequence

# Approach
> Convert the input string into a hash map of indices, then check each string to see whether it is a subsequence

# Code
```Python3 []

class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        def helper(tmp: str) -> bool:
            idx = -1
            for c in tmp:
                nxt = bisect_left(d[c], idx + 1)
                if nxt == len(d[c]):
                    return False
                idx = d[c][nxt]
            return True

        d, ans = defaultdict(list), 0
        for i, c in enumerate(s):
            d[c].append(i)
        return sum(helper(word) for word in words)
```
