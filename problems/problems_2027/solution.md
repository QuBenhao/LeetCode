# [Python] 贪心模拟

> slug: python-tan-xin-mo-ni-by-himymben-3qip
> date: 2022-12-27
> tags: Go, Java, JavaScript, Python3, TypeScript
> question: Minimum Moves to Convert String (minimum-moves-to-convert-string)
> url: https://leetcode.cn/problems/minimum-moves-to-convert-string/solutions/bFuIYv/python-tan-xin-mo-ni-by-himymben-3qip/

---
注意最左边的X一定会消耗一次操作，那么就顺着从左往右依次找最左边的X即可

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