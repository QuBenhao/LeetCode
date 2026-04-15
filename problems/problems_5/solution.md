# [Python/Go] 中心扩展

> Author: Benhao
> Date: 2022-02-23
> Upvotes: 10
> Tags: Go, Python, Python3

---

### 解题思路
枚举每个奇偶长度的回文串的中心起点，找最长的可能性

### 代码

```Python3 []
class Solution:
    def longestPalindrome(self, s: str) -> str:
        res, n = "", len(s)
        for i in range(n):
            l = r = i
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
            if r - l - 1 > len(res):
                res = s[l+1:r]
            l, r = i, i + 1
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
            if r - l - 1 > len(res):
                res = s[l+1:r]
        return res
```
```Go []
func longestPalindrome(s string) (res string) {
    for i, n := 0, len(s); i < n; i++ {
        l, r := i, i
        for l >= 0 && r < n && s[l] == s[r] {
            l--
            r++
        }
        if r - l - 1 > len(res) {
            res = s[l+1:r]
        }
        l, r = i, i + 1
        for l >= 0 && r < n && s[l] == s[r] {
            l--
            r++
        }
        if r - l - 1 > len(res) {
            res = s[l+1:r]
        }
    }
    return 
}
```