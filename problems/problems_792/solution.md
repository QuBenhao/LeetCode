# [Python] 坐标哈希+二分

> Author: Benhao
> Date: 2022-11-16
> Upvotes: 8
> Tags: Go, Java, JavaScript, Python3, TypeScript

---

> Problem: [792. 匹配子序列的单词数](https://leetcode.cn/problems/number-of-matching-subsequences/description/)

[TOC]

# 思路
> 将字符串处理为按字符分类的坐标哈希数组, 这样对每个单词, 不断二分往后找下一个字符的坐标, 就可以判断是否是子序列了

# 解题方法
> 用哈希坐标将输入的字符串转换, 再依次判断每个字符串是否是子序列

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
