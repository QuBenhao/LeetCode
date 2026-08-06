# [Python/Go] 动态规划

> slug: pythongo-dong-tai-gui-hua-by-himymben-ijla
> date: 2022-02-19
> tags: Go, Python, Python3
> question: Minimum Falling Path Sum (minimum-falling-path-sum)
> url: https://leetcode.cn/problems/minimum-falling-path-sum/solutions/dlBqSn/pythongo-dong-tai-gui-hua-by-himymben-ijla/

---
### 解题思路
滚动更新，维护到达当前行每一列的最小值，最终到达最后一行返回最小的结果即可

### 代码

```Python3 []
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        m, n, dp = len(matrix), len(matrix[0]), [matrix[0]] + [[inf] * n]
        for i in range(1, m):
            for j in range(n):
                dp[i%2][j] = inf
                for k in (-1, 0, 1):
                    if 0 <= (nj := j + k) < n:
                        dp[i%2][j] = min(dp[i%2][j], dp[(i-1)%2][nj])
                dp[i%2][j] += matrix[i][j]
        return min(dp[(m - 1)%2])
```
```Go []
const inf int = 0x3f3f3f
func minFallingPathSum(matrix [][]int) int {
    m, n := len(matrix), len(matrix[0])
    dp := make([][]int, 2)
    dp[0], dp[1] = make([]int, n), make([]int, n)
    for i, v := range matrix[0] {
        dp[0][i] = v
        dp[1][i] = inf
    }
    for i := 1; i < m; i++ {
        for j := 0; j < n; j++ {
            dp[i&1][j] = inf
            for k := -1; k <= 1; k++ {
                if nj := j + k; nj >= 0 && nj < n {
                    dp[i&1][j] = min(dp[i&1][j], dp[(i-1)&1][nj])
                }
            }
            dp[i&1][j] += matrix[i][j]
        }
    }
    return minV(dp[(m-1)&1])
}
func min(a, b int) int {
    if a < b {
        return a
    }
    return b
}
func minV(vals []int) int {
    ans := vals[0]
    for _, v := range vals {
        if v < ans {
            ans = v
        }
    }
    return ans
}
```