# [Python/Java/JavaScript/Go] Two pointers

> slug: pythonjavajavascriptgo-shuang-zhi-zhen-b-szpf
> date: 2022-02-22
> tags: Go, Java, JavaScript, Python, Python3
> question: Reverse Only Letters (reverse-only-letters)
> url: https://leetcode.cn/problems/reverse-only-letters/solutions/5z7yoz/pythonjavajavascriptgo-shuang-zhi-zhen-b-szpf/

---
### Approach
This is a typical problem of swapping selected character types from the two ends, solved with two pointers.
The left pointer tracks the next character to swap on the left, and the right pointer does the same on the right.

### Code

```Python3 []
class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        chars, l, r = list(s), 0, len(s) - 1
        while l < r:
            while l < r and not ('a' <= s[l] <= 'z' or 'A' <= s[l] <= 'Z'):
                l += 1
            while r > l and not ('a' <= s[r] <= 'z' or 'A' <= s[r] <= 'Z'):
                r -= 1
            if l < r:
                chars[l], chars[r] = chars[r], chars[l]
                l += 1
                r -= 1
        return "".join(chars)
```
```Java []
class Solution {
    public String reverseOnlyLetters(String s) {
        char[] chars = s.toCharArray();
        for(int l = 0, r = chars.length - 1; l < r; ) {
            while(l < r && !((chars[l] >= 'a' && chars[l] <= 'z') || (chars[l] >= 'A' && chars[l] <= 'Z')))
                l++;
            while(r > l && !((chars[r] >= 'a' && chars[r] <= 'z') || (chars[r] >= 'A' && chars[r] <= 'Z')))
                r--;
            if(l < r) {
                char tmp = chars[l];
                chars[l++] = chars[r];
                chars[r--] = tmp;
            }
        }
        return String.valueOf(chars);
    }
}
```
```JavaScript []
/**
 * @param {string} s
 * @return {string}
 */
var reverseOnlyLetters = function(s) {
    const chars = s.split('')
    for(let l = 0, r = s.length - 1; l < r;) {
        while(l < r && !((chars[l] >= 'a' && chars[l] <= 'z') || (chars[l] >= 'A' && chars[l] <= 'Z')))
            l++
        while(r > l && !((chars[r] >= 'a' && chars[r] <= 'z') || (chars[r] >= 'A' && chars[r] <= 'Z')))
            r--
        if(l < r) {
            const tmp = chars[l]
            chars[l++] = chars[r]
            chars[r--] = tmp
        }
    }
    return chars.join("")
};
```
```Go []
func reverseOnlyLetters(s string) string {
    bytes := []byte(s)
    for l, r := 0, len(s) - 1; l < r; {
        for l < r && !((bytes[l] >= 'a' && bytes[l] <= 'z') || (bytes[l] >= 'A' && bytes[l] <= 'Z')) {
            l++
        }
        for l < r && !((bytes[r] >= 'a' && bytes[r] <= 'z') || (bytes[r] >= 'A' && bytes[r] <= 'Z')) {
            r--
        }
        if l < r {
            bytes[l], bytes[r] = bytes[r], bytes[l]
            l++
            r--
        }
    }
    return string(bytes)
}
```

One-liner (stack)
```python3
class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        return "".join([alpha.pop() if c.isalpha() else c for c in s]) if (alpha := [c for c in s if c.isalpha()]) else s
```
