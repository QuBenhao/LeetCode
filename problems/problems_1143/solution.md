# [Python/Go] 动态规划

> Author: Benhao
> Date: 2021-04-02
> Upvotes: 1
> Tags: Go, Python, Python3

---

### 解题思路
如果当前字符相同，那么当前最长公共序列等于前一次的最大长度加一
否则等于两者取一个作为末尾中的最大值

### 代码

```Python []
class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        m, n = len(text1), len(text2)
        dp = [[0] * (n+1) for _ in range(m+1)]
        for i in range(m):
            for j in range(n):
                if text1[i] == text2[j]:
                    dp[i+1][j+1] = dp[i][j] + 1
                else:
                    dp[i+1][j+1] = max(dp[i+1][j],dp[i][j+1])
        return dp[-1][-1]
```
```Python3 []
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m):
            for j in range(n):
                if text1[i] == text2[j]:
                    dp[i + 1][j + 1] = dp[i][j] + 1
                else:
                    dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])
        return dp[-1][-1]
```
```Go []
func longestCommonSubsequence(text1 string, text2 string) int {
    m, n := len(text1), len(text2)
    dp := make([][]int, m + 1)
    dp[0] = make([]int, n + 1)
    for i := 0; i < m; i++ {
        dp[i + 1] = make([]int, n + 1)
        for j := 0; j < n; j++ {
            if text1[i] == text2[j] {
                dp[i + 1][j + 1] = dp[i][j] + 1
            } else {
                dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])
            }
        }
    }
    return dp[m][n]
}

func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}
```