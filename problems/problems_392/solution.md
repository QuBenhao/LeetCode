# [Python/Go] Two pointers

> slug: pythongo-shuang-zhi-zhen-by-himymben-7gus
> date: 2022-02-24
> tags: Go, Python, Python3
> question: Is Subsequence (is-subsequence)
> url: https://leetcode.cn/problems/is-subsequence/solutions/Y5swky/pythongo-shuang-zhi-zhen-by-himymben-7gus/

---
### Approach
Track how much of s has been matched and check whether the entire string is covered.

### Code

```Python3 []
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = j = 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == len(s)
```
```Go []
func isSubsequence(s string, t string) bool {
    i := 0
    for j := 0; i < len(s) && j < len(t); j++ {
        if s[i] == t[j] {
            i++
        }
    }
    return i == len(s)
}
```

```Python3
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # TODO: KMP
```
