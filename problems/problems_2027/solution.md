# [Python] Greedy simulation

> slug: python-tan-xin-mo-ni-by-himymben-3qip
> date: 2022-12-27
> tags: Go, Java, JavaScript, Python3, TypeScript
> question: Minimum Moves to Convert String (minimum-moves-to-convert-string)
> url: https://leetcode.cn/problems/minimum-moves-to-convert-string/solutions/bFuIYv/python-tan-xin-mo-ni-by-himymben-3qip/

---
The leftmost X always requires one operation, so repeatedly find the leftmost remaining X while scanning from left to right.

```Python3 []
class Solution:
    def minimumMoves(self, s: str) -> int:
        ans = i = 0
        while i < len(s):
            if s[i] == 'X':
                ans += 1
                i += 3
            else:
                i += 1
        return ans
```
```Go []
func minimumMoves(s string) (ans int) {
    for i := 0; i < len(s); {
        if s[i] == 'X' {
            ans++
            i += 3
        } else {
            i++
        }
    }
    return
}
```
