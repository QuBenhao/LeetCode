# [Python/Go] Dynamic programming

> Author: Benhao
> Date: 2022-02-25
> Upvotes: 1
> Tags: Go, Python, Python3

---

### Approach
Let dp[i][j] represent the minimum edit distance between word1[:i] and word2[:j].
If word1[i] equals word2[j], the new minimum edit distance dp[i+1][j+1] is the previous minimum dp[i][j];
otherwise, obtain the new minimum by deleting word1[i] from word1, deleting the character at j from word2, or replacing word1[i] or word2[j] to make them equal: min(dp[i+1][j], dp[i][j+1], dp[i][j]) + 1.

Initialize the case where one string is empty and the other is not: the edit cost is the nonempty string's length.

### Code

```Python3 []
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [[inf] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = 0
        for i in range(m):
            dp[i + 1][0] = i + 1
        for j in range(n):
            dp[0][j + 1] = j + 1
        for i in range(m):
            for j in range(n):
                if word1[i] == word2[j]:
                    dp[i + 1][j + 1] = dp[i][j]
                else:
                    dp[i + 1][j + 1] = min(dp[i][j + 1], dp[i + 1][j], dp[i][j]) + 1
        return dp[m][n]
```
```Go []
func minDistance(word1 string, word2 string) int {
    m, n := len(word1), len(word2)
    dp := make([][]int, m + 1)
    dp[0] = make([]int, n + 1)
    for j := 1; j <= n; j++ {
        dp[0][j] = j
    }
    for i := 0; i < m; i++ {
        dp[i + 1] = make([]int, n + 1)
        dp[i + 1][0] = i + 1
        for j := 0; j < n; j++ {
            if word1[i] == word2[j] {
                dp[i + 1][j + 1] = dp[i][j]
            } else {
                dp[i + 1][j + 1] = min(dp[i][j + 1], dp[i + 1][j], dp[i][j]) + 1
            }
        }
    }
    return dp[m][n]
}

func min(vals ...int) int {
    ans := vals[0]
    for _, v := range vals {
        if ans > v {
            ans = v
        }
    }
    return ans
}
```
