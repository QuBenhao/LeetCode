# [Python/Java] 双向哈希

> Author: Benhao
> Date: 2024-03-15
> Upvotes: 1
> Tags: C, Go, Java, Python3, TypeScript

---


> Problem: [290. 单词规律](https://leetcode.cn/problems/word-pattern/description/)

[TOC]

# 思路

> 记录一个 pattern字符到s中的子串的哈希，和一个s中的子串到pattern字符的哈希，遍历对比是否一致

# 解题方法

> 哈希

# 复杂度

时间复杂度:
> $O(n)$

空间复杂度:
> $O(n)$



# Code
```Python3 []
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        sp = s.split(" ")
        if len(sp) != len(pattern):
            return False
        mp1, mp2 = dict(), dict()
        for c, st in zip(pattern, sp):
            if c in mp1:
                if mp1[c] != st:
                    return False
            else:
                mp1[c] = st
            if st in mp2:
                if mp2[st] != c:
                    return False
            else:
                mp2[st] = c
        return True
```
```Java []
class Solution {
    public boolean wordPattern(String pattern, String s) {
        String[] splits = s.split(" ");
        if (splits.length != pattern.length()) {
            return false;
        }
        Map<Character, String> mp1 = new HashMap<>();
        Map<String, Character> mp2 = new HashMap<>();
        for (int i = 0; i < pattern.length(); i++) {
            if (mp1.containsKey(pattern.charAt(i))) {
                if (splits[i].compareTo(mp1.get(pattern.charAt(i))) != 0) {
                    return false;
                }
            }
            if (mp2.containsKey(splits[i])) {
                if (pattern.charAt(i) != mp2.get(splits[i])) {
                    return false;
                }
            }
            mp1.put(pattern.charAt(i), splits[i]);
            mp2.put(splits[i], pattern.charAt(i));
        }
        return true;
    }
}
```
  
