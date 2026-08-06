# [Go] 建切片，错位赋值

> slug: go-jian-qie-pian-cuo-wei-fu-zhi-by-himym-viwq
> date: 2021-11-12
> tags: Go, Python, Python3
> question: 动态口令 (zuo-xuan-zhuan-zi-fu-chuan-lcof)
> url: https://leetcode.cn/problems/zuo-xuan-zhuan-zi-fu-chuan-lcof/solutions/f4uqqB/go-jian-qie-pian-cuo-wei-fu-zhi-by-himym-viwq/

---
```Golang []
func reverseLeftWords(s string, n int) string {
    ans := make([]byte, len(s))
    for i := range s {
        if i < n {
            ans[len(s) - n + i] = s[i]
        } else {
            ans[i - n] = s[i] 
        }
    }
    return string(ans)
}
```
```Python3 []
class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        return s[n:] + s[:n]
```