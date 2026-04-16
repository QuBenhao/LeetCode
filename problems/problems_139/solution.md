# [Python/Go] 动态规划

> Author: Benhao
> Date: 2022-02-15
> Upvotes: 1
> Tags: C, Go, Java, Python, Python3

---

### 解题思路
有任意子串在字典中存在时，该结尾可以由前面构成的情况构成

### 代码

```Python3 []
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n, words, ml = len(s), set(wordDict), max(len(word) for word in wordDict)
        cur = {0}
        for i in range(1, n + 1):
            tmp = set(cur)
            for idx in tmp:
                if i - idx > ml:
                    cur.remove(idx)
                    continue
                if idx < i and s[idx:i] in words:
                    cur.add(i)
                    break
        return n in cur
```
```Go []
func wordBreak(s string, wordDict []string) bool {
    n := len(s)
    dp := make([]bool, n + 1)
    dp[0] = true
    for i := 0; i < n; i++ {
        for _, word := range wordDict {
            if j := i + len(word); j <= n && s[i:j] == word {
                if dp[i] {
                    dp[j] = true
                }
            }
        }
    }
    return dp[n]
}
```