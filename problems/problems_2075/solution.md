# [Python/Go] 模拟

> slug: pythongo-mo-ni-by-himymben-9hu9
> date: 2021-11-14
> tags: Go, Python, Python3
> question: Decode the Slanted Ciphertext (decode-the-slanted-ciphertext)
> url: https://leetcode.cn/problems/decode-the-slanted-ciphertext/solutions/QZ9QrP/pythongo-mo-ni-by-himymben-9hu9/

---
```Python3 []
class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        def read(sy):
            sx = 0
            while sx < m and sy < n:
                ans.append(encodedText[sx * n + sy])
                sx += 1
                sy += 1
                
        ans = []
        m, n = rows, len(encodedText) // rows
        y = 0
        while y < n:
            read(y)
            y += 1
        while ans and ans[-1] == ' ':
            ans.pop()
        return "".join(ans)
```
```Go []
func decodeCiphertext(encodedText string, rows int) string {
    ans := make([]byte, 0)
    for j, m, n := 0, rows, len(encodedText)/rows; j < n; j++ {
        for i, k := 0, j; i < m && k < n; i++ {
            ans = append(ans, encodedText[i * n + k])
            k++
        }
    }
    for i := len(ans) - 1; i >= 0 && ans[i] == byte(' '); i--{
        ans = ans[:i]
    }
    return string(ans)
}
```