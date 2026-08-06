# [Python/Go/C] 双指针模拟

> slug: pythongoc-shuang-zhi-zhen-mo-ni-by-himym-x5jz
> date: 2024-02-29
> tags: C, Go, Java, Python3, TypeScript
> question: Valid Palindrome (valid-palindrome)
> url: https://leetcode.cn/problems/valid-palindrome/solutions/JlUekE/pythongoc-shuang-zhi-zhen-mo-ni-by-himym-x5jz/

---

> Problem: [125. 验证回文串](https://leetcode.cn/problems/valid-palindrome/description/)

[TOC]

# 思路

> 左边和右边的指针不停比较

# 解题方法

> 双指针模拟

# 复杂度

时间复杂度:
> $O(n)$

空间复杂度:
> $O(1)$



# Code
```Python3 []
class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            if s[left].upper() != s[right].upper():
                return False
            left += 1
            right -= 1
        return True
```
```Go []
func isalumn(b byte) bool {
    return (b >= 'a' && b <= 'z') || (b >= 'A' && b <= 'Z') || (b >= '0' && b <= '9')
}
func isPalindrome(s string) bool {
    s = strings.ToLower(s)
    for left, right := 0, len(s) - 1; left < right; left++ {
        for left < right && !isalumn(s[left]) {
            left++
        }
        for left < right && !isalumn(s[right]) {
            right--
        }
        if s[left] != s[right] {
            return false
        }
        right--
    }
    return true
}
```
```C []
bool isalumn(char c) {
    return (c >= 'a' && c <= 'z') || (c >= 'A' && c <= 'Z') || (c >= '0' && c <= '9');
}

bool isPalindrome(char* s) {
    for (int left = 0, right = strlen(s) - 1; left < right; left++, right--) {
        while (left < right && !isalumn(s[left])) {
            left++;
        }
        while (left < right && !isalumn(s[right])) {
            right--;
        }
        if (tolower(s[left]) != tolower(s[right])) {
            return false;
        }
    }
    return true;
}
```
  
