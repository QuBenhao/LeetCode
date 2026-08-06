# [Python/Go] 双指针

> slug: pythongo-shuang-zhi-zhen-by-himymben-7gus
> date: 2022-02-24
> tags: Go, Python, Python3
> question: Is Subsequence (is-subsequence)
> url: https://leetcode.cn/problems/is-subsequence/solutions/Y5swky/pythongo-shuang-zhi-zhen-by-himymben-7gus/

---
### 解题思路
记录s中的被匹配到的位置，看看最后能否覆盖整个字符串。

### 代码

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