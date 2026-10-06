# [Python/Java] Bidirectional hash maps

> Author: Benhao
> Date: 2024-03-15
> Upvotes: 1
> Tags: C, Go, Java, Python3, TypeScript

---


> Problem: [290. 单词规律](https://leetcode.cn/problems/word-pattern/description/)

[TOC]

# Intuition

> Record a map from pattern characters to words in s and another from words in s to pattern characters, then traverse and check consistency.

# Approach

> Hashing

# Complexity

Time complexity:
> $O(n)$

Space complexity:
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
  
