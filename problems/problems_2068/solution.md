# [Python/Go] 模拟

> slug: pythongo-mo-ni-by-himymben-owf2
> date: 2021-11-13
> tags: Go, Python, Python3
> question: Check Whether Two Strings are Almost Equivalent (check-whether-two-strings-are-almost-equivalent)
> url: https://leetcode.cn/problems/check-whether-two-strings-are-almost-equivalent/solutions/hrTMrr/pythongo-mo-ni-by-himymben-owf2/

---
```Python3 []
class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        c1, c2 = Counter(word1), Counter(word2)
        return all(abs(c1[k] - c2[k]) <= 3 for k in c1.keys() | c2.keys())
```
```Go []
func checkAlmostEquivalent(word1 string, word2 string) bool {
    c1, c2 := map[byte]int{}, map[byte]int{}
    for i := range word1 {
        c1[word1[i]] += 1
    }
    for i := range word2 {
        c2[word2[i]] += 1
    }
    base := 97
    for i := 0; i < 26; i++ {
        b := byte(base)
        if v := c1[b] - c2[b]; v > 3 || v < -3 {
            return false
        }
        base++
    }
    return true
}
```