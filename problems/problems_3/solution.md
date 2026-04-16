# [Python/Java/Go/C/Ts] 滑动窗口

> Author: Benhao
> Date: 2024-03-06
> Upvotes: 1
> Tags: C, Go, Java, Python3, TypeScript

---


> Problem: [3. 无重复字符的最长子串](https://leetcode.cn/problems/longest-substring-without-repeating-characters/description/)

[TOC]

# 思路

> 题目要求的是子串，当我们遇到相同字符时，需要将子串起始位置移动到上一个相同字符之后，这符合滑动窗口的思想

# 解题方法

> 滑动窗口

# 复杂度

时间复杂度:
> $O(n)$

空间复杂度:
> $O(n)$



# Code
```Python3 []
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans, window = 0, set()
        for i, c in enumerate(s):
            while c in window:
                window.remove(s[i - len(window)])
            window.add(c)
            ans = max(ans, len(window))
        return ans
```
```Java []
class Solution {
    public int lengthOfLongestSubstring(String s) {
        int ans = 0;
        Set<Character> window = new HashSet<>();
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            while (window.contains(c)) {
                window.remove(s.charAt(i - window.size()));
            }
            window.add(c);
            ans = Math.max(ans, window.size());
        }
        return ans;
    }
}
```
```Go []
func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}

func lengthOfLongestSubstring(s string) (ans int) {
    window := map[rune]bool{}
    for i, ch := range s {
        for window[ch] {
            delete(window, rune(s[i - len(window)]))
        }
        window[ch] = true
        ans = max(ans, len(window))
    }
    return
}
```
```C []
int lengthOfLongestSubstring(char* s) {
    int ans = 0;
    bool window[256];
    bzero(window, sizeof(bool) * 256);
    for (int i = 0, length = 0; i < strlen(s); i++) {
        int c = toascii(s[i]);
        while (window[c]) {
            window[toascii(s[i - length--])] = false;
        }
        window[c] = true;
        ans = ++length > ans ? length : ans;
    }
    return ans;
}
```
```TypeScript []
function lengthOfLongestSubstring(s: string): number {
    const window = new Set();
    let ans: number = 0;
    for (let i = 0; i < s.length; i++) {
        const c = s.charAt(i);
        while(window.has(c)) {
            window.delete(s.charAt(i - window.size));
        }
        window.add(c);
        ans = Math.max(ans, window.size);
    }
    return ans;
};
```
```C++ []
class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        unordered_map<char, int> map;
        int ans = 0;
        for (int i = 0, j = -1; i < s.length(); i++) {
            if (map.find(s[i]) != map.end()) {
                j = max(j, map[s[i]]);
            }
            ans = max(ans, i - j);
            map[s[i]] = i;
        }
        return ans;
    }
};
```

