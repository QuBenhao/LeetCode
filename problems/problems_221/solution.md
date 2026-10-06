# [Python/Go] Dynamic programming (rolling updates)

> Author: Benhao
> Date: 2022-02-22
> Upvotes: 1
> Tags: Go, Python, Python3

---

### Approach
The largest square ending at the current cell has side length one plus the minimum of the largest square side lengths at the upper-left, upper, and left cells.
For example, if the upper-left cell can form only a square of side length 1, the current cell can form a square of side length at most 2.
Similarly, the upper and left cells also constrain the current cell.

### Code

```Python3 []
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        ans, m, n = 0, len(matrix), len(matrix[0])
        dp = [[0] * n for _ in range(2)]
        for i in range(m):
            for j in range(n):
                b = matrix[i][j] == '1'
                dp[i&1][j] = int(b)
                if i and j and b:
                    dp[i&1][j] = 1 + min(dp[(i - 1)&1][j - 1], dp[(i - 1)&1][j], dp[i&1][j - 1])
                ans = max(ans, dp[i&1][j])
        return ans ** 2
```
```Go []
func maximalSquare(matrix [][]byte) (ans int) {
    m, n := len(matrix), len(matrix[0])
    dp := make([][]int, 2)
    dp[0], dp[1] = make([]int, n), make([]int, n)
    for i := 0; i < m; i++ {
        for j := 0; j < n; j++ {
            if matrix[i][j] == '1' {
                dp[i & 1][j] = 1
                if i > 0 && j > 0{
                    dp[i & 1][j] += min(dp[(i - 1) & 1][j], dp[(i - 1) & 1][j - 1], dp[i & 1][j - 1])
                }
                ans = max(ans, dp[i & 1][j])
            } else {
                dp[i & 1][j] = 0
            }
        }
    }
    ans *= ans
    return
}

func min(vals ...int) int {
    ans := vals[0]
    for _, v := range vals {
        if v < ans {
            ans = v
        }
    }
    return ans
}

func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}
```
